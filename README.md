📄 PDF Q&A with Local LLMs
This is a simple web application built with Streamlit and LangChain that allows you to chat with your PDF documents. It uses local models via Ollama, ensuring your data remains private and secure on your machine.

Features
Multiple PDF Uploads: Process and query one or more PDF documents simultaneously.

Local & Private: All processing happens locally using Ollama. No data is sent to external APIs.

Source Referencing: The app shows which parts of the documents were used to generate the answer.

Simple UI: Easy-to-use interface for uploading files and asking questions.

⚙️ Setup and Installation Guide
Follow these steps to get the application running on your local machine.

1. Prerequisites
Make sure you have the following software installed:

Python 3.8+

Ollama: Download and install from the official Ollama website.

2. Clone the Repository
First, get the project files on your local machine. If you are using git, you can clone the repository:

git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name

Otherwise, just create a folder and place app.py and requirements.txt inside it.

3. Install Dependencies
It is highly recommended to use a Python virtual environment to avoid conflicts with other projects.

Create and activate the environment:

On macOS / Linux:

python3 -m venv venv
source venv/bin/activate

On Windows:

python -m venv venv
.\venv\Scripts\activate

Install the required packages from requirements.txt:

pip install -r requirements.txt

4. Download Ollama Models
This application requires two specific models from Ollama. Ensure the Ollama desktop application is running before proceeding.

Open your terminal and pull the necessary models:

# Pull the embedding model for creating vector representations
ollama pull nomic-embed-text

# Pull the language model for generating answers
ollama pull gemma:2b

▶️ How to Run the Application
Once the setup is complete, you can launch the application with a single command from your project directory:

streamlit run app.py

This will start the local server and open the application in a new tab in your default web browser. You can now upload your PDFs and start asking questions! 🚀

🛠️ Configuration
You can easily change the models or the text processing parameters by editing the CONFIG section at the top of the app.py file:

# ---------- CONFIG ----------
EMBED_MODEL = "nomic-embed-text"
LLM_MODEL = "gemma:2b"      # small + fast
CHUNK_SIZE = 800
CHUNK_OVERLAP = 100
