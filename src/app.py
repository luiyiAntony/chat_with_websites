import streamlit as st
import uuid
import json
import os
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

import chromadb

load_dotenv()

def populate_vectorstore_from_url(url, collection_name):

    # get the textin document form
    loader = WebBaseLoader(url)
    document = loader.load()

    # split the document into chunks
    text_splitter = RecursiveCharacterTextSplitter()
    document_chunks = text_splitter.split_documents(document)

    # create a vector store from the chunks
    #vector_store = chroma.Chroma.from_documents(document_chunks, OpenAIEmbeddings())
    vector_store = Chroma.from_documents(document_chunks, SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2"), collection_name=collection_name)
    return vector_store

def get_vectorstore(url):
    # check if the url is in the visited_urls file
    if visited_url(url):
        persistent_client = chromadb.PersistentClient("./db/")
        vectorstore = Chroma(
            client=persistent_client,
            collection_name=get_collection_name(url),
            persist_directory="./db/",
            embedding_function=SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        )
        return vectorstore
    else:
        vectorstore = create_vectorstore(url) # vectorstore
        return vectorstore
        
def get_collection_name(url):
    with open("./db/visited_urls.json", "r") as f:
        data = json.load(f)
    return data[url]

def create_vectorstore(url):
    coll_name = str(uuid.uuid4())
    # creamos un nuevo vectorstore
    vectorstore = populate_vectorstore_from_url(url, coll_name)
    # guardamos un nuevo registro de url y su collection_name
    with open("./db/visited_urls.json", "r") as f:
        data = json.load(f)
        data[url] = coll_name
    with open("./db/visited_urls.json", "w") as f:
        json.dump(data, f)
    return vectorstore

def visited_url(url):
    # verificar que el archivo exista
    if not os.path.isfile("./db/visited_urls.json"):
        with open("./db/visited_urls.json", "w") as f:
            json.dump({}, f)
    #
    with open("./db/visited_urls.json", "r") as f:
        data = json.load(f)
    return url in data

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
        "input": user_query
    })
    #return response['answer']
    return response

# app config
st.set_page_config(page_title="Chat websites", page_icon="")
st.title("Chat with websites")

# sidebar
with st.sidebar:
    website_url = st.text_input("Website URL")

if website_url is None or website_url == "":
    st.info("Please enter a website URL")
else:
    # session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            AIMessage(content="Hello, I'm a bot how can I help you?"),
        ]
    if "vector_store" not in st.session_state:
        st.session_state.vector_store = get_vectorstore(website_url)

    # user input
    user_query = st.chat_input("Type your message here...")
    if user_query is not None and user_query != "":
        response = get_response(user_query)
        st.write(response)
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        st.session_state.chat_history.append(AIMessage(content=response))

    # conversation
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("ai"):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("human"):
                st.write(message.content)