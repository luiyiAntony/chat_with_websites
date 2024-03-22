import streamlit as st
from streamlit.logger import get_logger
import uuid
import json
import os
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from chromadb import Collection

import chromadb

load_dotenv()
logger = get_logger(__name__)

def populate_vectorstore_from_url(url, collection_name):

    # get the textin document form
    loader = WebBaseLoader(url)
    document = loader.load()

    # split the document into chunks
    text_splitter = RecursiveCharacterTextSplitter()
    document_chunks = text_splitter.split_documents(document)

    # create a vector store from the chunks
    #vector_store = chroma.Chroma.from_documents(document_chunks, OpenAIEmbeddings())
    vector_store = Chroma.from_documents(
        document_chunks, 
        SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2"), 
        collection_name=collection_name,
        persist_directory="./db/")
    return vector_store

def get_vectorstore(url):
    # check if the url is in the visited_urls file
    if visited_url(url):
        logger.info("getting vectorstore")
        persistent_client = chromadb.PersistentClient("./db/")
        vectorstore = Chroma(
            client=persistent_client,
            collection_name=get_collection_name(url),
            persist_directory="./db/",
            embedding_function=SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        )
        return vectorstore
    else:
        logger.info("CREATING vectorstore")
        vectorstore = create_vectorstore(url) # vectorstore
        return vectorstore
        
def get_collection_name(url):
    with open("./db/visited_urls.json", "r") as f:
        data = json.load(f)
    return data[url]["collection_name"]

def create_vectorstore(url):
    coll_name = str(uuid.uuid4())
    # creamos un nuevo vectorstore
    vectorstore = populate_vectorstore_from_url(url, coll_name)
    # guardamos un nuevo registro de url y su collection_name
    data = get_visited_urls() # diccionary
    data[url] = {"collection_name": coll_name}
    guardar_visited_urls_data(data)
    return vectorstore

def update_vectorstore(url):
    # recuperar el chat_history
    chat_history = get_chat_history(url) # messages
    # eliminar el vectorstore
    delete_vectorstore(url)
    # crear un nuevo vectorstore
    _ = create_vectorstore(url) # vectorstore
    # setear en chat_history
    data = get_visited_urls() # diccionario (leido con json.load() desde el archivo)
    data[url]["chat_history"] = message_to_dic(chat_history)
    guardar_visited_urls_data(data)

def delete_vectorstore(url):
    vectorstore = get_vectorstore(url)
    # eliminamos el embedding
    vectorstore.delete_collection()
    # eliminamos los datos en el archivo .json
    data = get_visited_urls()
    data.pop(url)
    guardar_visited_urls_data(data)

def guardar_visited_urls_data(_data):
    try:
        with open("./db/visited_urls.json", "r") as f:
            data = json.load(f)
        respaldo = data
        data = _data
        with open("./db/visited_urls.json", "w") as f:
            json.dump(data, f)
    except:
        data = respaldo
        with open("./db/visited_urls.json", "w") as f:
            json.dump(data, f)

def visited_url(url):
    # verificar que el archivo exista
    if not os.path.isfile("./db/visited_urls.json"):
        with open("./db/visited_urls.json", "w") as f:
            json.dump({}, f)
    #
    with open("./db/visited_urls.json", "r") as f:
        data = json.load(f)
    return url in data

def get_visited_urls():
    # verificar que el archivo exista
    if not os.path.isfile("./db/visited_urls.json"):
        with open("./db/visited_urls.json", "w") as f:
            json.dump({}, f)
    #
    with open("./db/visited_urls.json", "r") as f:
        data = json.load(f)
    return data

def get_context_retriever_chain(vector_store):
    llm = ChatOpenAI()
    retriever = vector_store.as_retriever()
    prompt = ChatPromptTemplate.from_messages([
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}"), # this input will be populated with whatever we pass in
        ("user", "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation")
    ])
    retriever_chain = create_history_aware_retriever(llm, retriever, prompt)
    return retriever_chain

def get_conversational_rag_chain(retriever_chain):
    llm = ChatOpenAI()
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Answer the user's questions based on the below context:\n\n{context}"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}")
    ])

    stuff_documents_chain = create_stuff_documents_chain(llm, prompt)

    return create_retrieval_chain(retriever_chain, stuff_documents_chain)

def get_response(user_input):
    retriever_chain = get_context_retriever_chain(st.session_state.vector_store) #
    conversation_rag_chain = get_conversational_rag_chain(retriever_chain) #

    response = conversation_rag_chain.invoke({
        "chat_history": st.session_state.chat_history,
        "input": user_input
    })
    return response['answer']

def get_chat_history(website_url):
    data = get_visited_urls()
    if website_url not in data.keys():
        data[website_url] = {}
    sub_data = data[website_url]
    if "chat_history" not in sub_data.keys():
        chat_history = [
            AIMessage(content="Hello, I'm a bot how can I help you?"),
        ]
    else:
        chat_history = dic_to_message(sub_data["chat_history"])
    return chat_history

def guardar_chat(url, _chat_history):
    data = get_visited_urls()
    chat_history = message_to_dic(_chat_history)
    if (isinstance(data[url], str)):
        cadena_url = data[url]
        data[url] = {"collection_name" : cadena_url}
        data[url]["chat_history"] = chat_history
    else:
        data[url]["chat_history"] = chat_history
    guardar_visited_urls_data(data)

def dic_to_message(dicc_history):
    new_history = []
    for message in dicc_history:
        if "ai" in message.keys():
            msg = AIMessage(content=message["ai"])
        elif "human" in message.keys():
            msg = HumanMessage(content=message["human"])
        else:
            msg = SystemMessage(content="Error en la matrix, no se pudo recuperar el mensage")
        new_history.append(msg)
    return new_history

def message_to_dic(history):
    new_history = []
    for message in history:
        if (isinstance(message, HumanMessage)):
            msg = {"human": message.content}
        elif (isinstance(message, AIMessage)):
            msg = {"ai": message.content}
        else:
            msg = {"matrix": "error en la matrix, no se pudo recuperar el mensage"}
        new_history.append(msg)
    return new_history

def change_url(url):
    st.session_state.clear()
    st.session_state["website_url"] = url
    logger.info("change_url function")

def change_input_url():
    url = st.session_state["website_url"]
    st.session_state.clear()
    st.session_state["website_url"] = url
    logger.info("change_input_url function")

###################################################
# RELATED WITH THE INTERFACE
###################################################

def check_session_state():
    if "vector_store" not in st.session_state:
        st.session_state.vector_store = get_vectorstore(website_url)
        #logger.info(st.session_state.vector_store.get())
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = get_chat_history(website_url)

def chat():
    # user input
    user_query = st.chat_input("Type your message here...")
    if user_query is not None and user_query != "":
        response = get_response(user_query)
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        st.session_state.chat_history.append(AIMessage(content=response))
        guardar_chat(st.session_state.website_url, st.session_state.chat_history)

    # conversation
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("ai"):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("human"):
                st.write(message.content)


# app config
st.set_page_config(page_title="Chat websites", page_icon="")
st.title("Chat with websites")

st.markdown(
    f'''
        <style>
            .sidebar .sidebar-content {{
                padding: 15px;
            }}
            .st-emotion-cache-16txtl3 {{
                padding-top: 15%;
            }}
        </style>
    ''',
    unsafe_allow_html=True
)

# sidebar
with st.sidebar:
    website_url = st.text_input("New Website URL", key="website_url", on_change=change_input_url)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Actualizar"):
            update_vectorstore(website_url)
            st.info("Actualizando informacion")
            
    with col2:
        if st.button("Eliminar"):
            delete_vectorstore(website_url)
            website_url = ""
            st.warning("Eliminando informacion")
    st.write("Previous URLs")
    with st.container(height=330, border=0):
        urls = get_visited_urls()
        for url in urls:
            st.button(url, on_click=change_url, args=[url])

if website_url is None or website_url == "":
    st.info("Please enter a website URL")
else:
    # session state
    check_session_state()

    # chat
    chat()