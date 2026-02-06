import chromadb
from sentence_transformers import SentenceTransformer
from src.llm import generate_response

CHROMA_PATH = "chroma_db"

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = chroma_client.get_collection(name="med_docs")

def ask_rag(question: str):
    query_embedding = embedding_model.encode([question]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )

    docs = results["documents"][0]
    metadatas = results["metadatas"][0]

    context = "\n\n".join(docs)

    prompt = f"""
You are WHOAssist, an assistant for knowledge base in World Healthcare Organization.

Answer ONLY using the provided documents.
If the answer is not in the context, say:
"I don’t have that information in the knowledge base."

Context:
{context}

Question: {question}
"""

    answer = generate_response(prompt)

    sources = list(set(meta["source"] for meta in metadatas))

    return answer, sources
