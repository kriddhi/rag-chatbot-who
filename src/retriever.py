import chromadb
from chromadb.utils import embedding_functions

CHROMA_PATH = "chroma_db/"

embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = client.get_collection(name="documents", embedding_function=embedding_function)

def retrieve_context(query, k=3):
    results = collection.query(query_texts=[query], n_results=k)

    docs = results["documents"][0]
    metas = results["metadatas"][0]

    context = ""
    sources = set()

    for doc, meta in zip(docs, metas):
        context += f"\nSource: {meta['source']}\n{doc}\n"
        sources.add(meta["source"])

    return context, list(sources)
