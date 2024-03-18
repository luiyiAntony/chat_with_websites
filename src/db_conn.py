import chromadb
import uuid
import json
from langchain_community.vectorstores import chroma

client = chromadb.PersistentClient(path="./db") # the path is where Chroma will store its database files on disk and load them on start

# web_coll = client.get_or_create_collection(name="web_sites")
# music_coll = client.get_or_create_collection(name="music_lyrics")

# web_coll.add(
#     documents=["Contenido de una pagina web ... "],
#     metadatas=[{"url": "https://pagina.com/info"}],
#     ids=["doc1"]
# )

# music_coll.add(
#     documents=["one last kiss"],
#     metadatas=[{"url": "https://youtube.com/one_last_kiss"}],
#     ids=["music1"]
# )

def get_vectorstore(url):
    coll_name = str(uuid.uuid4())
    persistent_client = chromadb.PersistentClient("../db")
    collection = persistent_client.get_or_create_collection(coll_name)
    langchain_chroma = chroma.Chroma(
        client=persistent_client,
        collection_name=coll_name,
    )
    print("There are", langchain_chroma._collection.count(), "in the collection")

dicc = {"a": 1, "b": 2}
with open("./db/data.json", "w") as f:
    json.dump(dicc, f)

with open("./db/data.json", "r") as file:
    data = json.load(file)
    print("a" in data)

# collection.query(
#     query_embeddings=[[11.1, 12.1, 13.1], [1.1, 2.3, 3.2]],
#     n_results=10,
#     where={"chapter": "16"},
#     where_document={"$contains":"doc2"}
# )









