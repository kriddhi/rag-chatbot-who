import os
import chromadb
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

DATA_PATH = "data"
CHROMA_PATH = "chroma_db"

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize Chroma client
chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = chroma_client.get_or_create_collection(name="med_docs")

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

documents = []
metadatas = []
ids = []

doc_id = 0

for file in os.listdir(DATA_PATH):
    if file.endswith(".pdf"):
        reader = PdfReader(os.path.join(DATA_PATH, file))
        text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
        chunks = text_splitter.split_text(text)

        for chunk in chunks:
            documents.append(chunk)
            metadatas.append({"source": file})
            ids.append(str(doc_id))
            doc_id += 1

# Generate embeddings
embeddings = embedding_model.encode(documents).tolist()

collection.add(
    documents=documents,
    embeddings=embeddings,
    metadatas=metadatas,
    ids=ids
)

print("✅ Documents ingested successfully!")
