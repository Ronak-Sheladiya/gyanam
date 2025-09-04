# Offline PDF Chat with Ollama - README

## Project Overview
This project is an offline RAG (Retrieval-Augmented Generation) system that allows you to chat with the contents of a PDF using local LLMs via Ollama and LangChain.

## Prerequisites
- Windows OS
- Python 3.8+
- [Ollama](https://ollama.com/download) installed and model pulled (e.g., llama2)

## Setup Instructions

### 1. Clone or Download the Project
Place all files in a folder, e.g., `D:\chatpdf`.

### 2. Create and Activate a Virtual Environment
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install Python Dependencies
```powershell
pip install streamlit langchain langchain-community langchain-ollama pypdf faiss-cpu
```

### 4. Install and Start Ollama
- Download and install Ollama from [Ollama Download](https://ollama.com/download)
- Pull a model (e.g., llama2):
```powershell
ollama pull llama2
```
- Start Ollama server (if not already running):
```powershell
ollama serve
```

### 5. Start the Streamlit App
```powershell
python -m streamlit run app.py
```

## Usage
- Upload a PDF using the web interface.
- Ask questions about the PDF content.
- All processing and LLM inference is done locally/offline.

## Troubleshooting
- If you see missing package errors, install them in your `.venv` using `pip install <package>`.
- If Ollama model memory errors occur, try a smaller or quantized model from the [Ollama library](https://ollama.com/library).
- Make sure you always activate your `.venv` before running commands.

## Example Commands (from scratch)
```powershell
# Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install streamlit langchain langchain-community langchain-ollama pypdf faiss-cpu

# Install Ollama and pull model
ollama pull llama2
ollama serve

# Run the app
python -m streamlit run app.py
```

---
For further help, see the Ollama and LangChain documentation.
