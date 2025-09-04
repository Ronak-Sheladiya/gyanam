from typing import List
from sentence_transformers import SentenceTransformer
import chromadb

class VectorStore:
    def __init__(self, persist_directory="./chroma_db"):
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection(
            name="documents",
            metadata={"hnsw:space": "cosine"}
        )
        
    def add_documents(self, chunks: List[str], metadata: List[dict] = None):
        """Add document chunks to vector store"""
        embeddings = self.embedding_model.encode(chunks).tolist()
        ids = [f"doc_{i}" for i in range(len(chunks))]
        self.collection.add(
            embeddings=embeddings,
            documents=chunks,
            metadatas=metadata or [{}] * len(chunks),
            ids=ids
        )
        
    def similarity_search(self, query: str, k: int = 5) -> List[str]:
        """Retrieve most relevant chunks for query"""
        query_embedding = self.embedding_model.encode([query]).tolist()
        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=k
        )
        return results['documents'][0]
