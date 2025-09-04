import os
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_ollama import OllamaLLM
from langchain.chains import ConversationalRetrievalChain

print("Import successful!")
# ----------------- SETUP -----------------
st.set_page_config(page_title="Offline RAG with Ollama", layout="wide")

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ----------------- UPLOAD PDF -----------------
st.title("📄 Offline PDF Chat with Ollama")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    pdf_path = os.path.join("uploaded_docs", uploaded_file.name)
    os.makedirs("uploaded_docs", exist_ok=True)
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Load & split
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)

    # Embeddings & Vectorstore
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    st.session_state.vectorstore = FAISS.from_documents(chunks, embeddings)

    st.success("✅ PDF uploaded & indexed successfully!")

# ----------------- CHAT SECTION -----------------
if st.session_state.vectorstore:
    query = st.chat_input("Ask something from the PDF...")

    if query:
        llm = OllamaLLM(model="llama2")  # change to your installed model
        qa = ConversationalRetrievalChain.from_llm(
            llm,
            retriever=st.session_state.vectorstore.as_retriever(),
            return_source_documents=True
        )

        result = qa.invoke({"question": query, "chat_history": st.session_state.chat_history})

        # Store history
        st.session_state.chat_history.append((query, result["answer"]))

        # Display conversation
        for q, a in st.session_state.chat_history:
            with st.chat_message("user"):
                st.write(q)
            with st.chat_message("assistant"):
                st.write(a)
