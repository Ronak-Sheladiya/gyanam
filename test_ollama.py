import requests

# Test Ollama API connection
url = "http://localhost:11434/api/generate"
payload = {
    "model": "mistral",
    "prompt": "Hello!",
    "stream": False
}
try:
    response = requests.post(url, json=payload)
    print("Status Code:", response.status_code)
    print("Response:", response.text)
except Exception as e:
    print("Error connecting to Ollama:", str(e))
