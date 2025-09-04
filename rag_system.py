from document_processor import DocumentProcessor
from vector_store import VectorStore
from offline_llm import OfflineLLM

class RAGSystem:
    def __init__(self):
        self.doc_processor = DocumentProcessor()
        self.vector_store = VectorStore()
        self.llm = OfflineLLM()
        
    def ingest_document(self, file_path: str):
        """Process and store a document"""
        text = self.doc_processor.extract_text(file_path)
        chunks = self.doc_processor.chunk_text(text)
        metadata = [{"source": file_path, "chunk_id": i} for i in range(len(chunks))]
        self.vector_store.add_documents(chunks, metadata)
        print(f"Ingested {len(chunks)} chunks from {file_path}")
        
    def query(self, question: str, top_k: int = 5):
        """Answer question using RAG pipeline"""
        relevant_chunks = self.vector_store.similarity_search(question, top_k)
        prompt = self.llm.create_rag_prompt(question, relevant_chunks)
        answer = self.llm.generate_response(prompt)
        return answer, relevant_chunks
