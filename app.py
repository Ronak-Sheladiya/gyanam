import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain.chains import RetrievalQA
import os


# ---------- CONFIG ----------
EMBED_MODEL = "nomic-embed-text"
LLM_MODEL = "gemma:2b"   # small + fast
CHUNK_SIZE = 800
CHUNK_OVERLAP = 100

# Store indexes per PDF
VECTOR_DB = {}

st.set_page_config(page_title="📄 PDF Q&A", layout="wide")
st.title("📄 PDF Question Answering App")

# --------- PDF Upload ----------
uploaded_files = st.file_uploader("Upload one or more PDFs", type="pdf", accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        pdf_name = uploaded_file.name

        if pdf_name not in VECTOR_DB:
            with st.spinner(f"Processing {pdf_name}..."):
                # Save temp file
                temp_path = os.path.join("docs", pdf_name)
                os.makedirs("docs", exist_ok=True)
                with open(temp_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())

                # Load PDF
                loader = PyPDFLoader(temp_path)
                pages = loader.load()

                # Split into chunks
                splitter = RecursiveCharacterTextSplitter(
                    chunk_size=CHUNK_SIZE,
                    chunk_overlap=CHUNK_OVERLAP
                )
                chunks = splitter.split_documents(pages)

                # Embeddings
                embeddings = OllamaEmbeddings(model=EMBED_MODEL)
                vectorstore = FAISS.from_documents(chunks, embeddings)

                # Save in dictionary
                VECTOR_DB[pdf_name] = vectorstore

    st.success("✅ PDFs processed! Ready to ask questions.")

    # Select PDF for Q&A
    selected_pdf = st.selectbox("Choose a PDF to query", list(VECTOR_DB.keys()))

    # Ask question
    user_q = st.text_input("Ask a question about the selected PDF:")

    if user_q:
        retriever = VECTOR_DB[selected_pdf].as_retriever()
        llm = OllamaLLM(model=LLM_MODEL)

        chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            return_source_documents=True
        )

        with st.spinner("Thinking..."):
            result = chain.invoke({"query": user_q})

        st.subheader("📌 Answer")
        st.write(result["result"])

        # Show references
        st.subheader("🔗 Sources")
        for doc in result["source_documents"]:
            st.write(f"Page: {doc.metadata.get('page_number', 'N/A')}")
            st.write(doc.page_content[:300] + "...")
            st.write("---")
