import requests
from typing import List

class OfflineLLM:
    def __init__(self, model_name="phi:2.7b", base_url="http://localhost:11434"):
        self.model_name = model_name
        self.base_url = base_url
        
    def generate_response(self, prompt: str) -> str:
        """Generate response using local Ollama model"""
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json()['response']
        else:
            raise Exception(f"Error: {response.status_code}")
            
    def create_rag_prompt(self, query: str, context: List[str]) -> str:
        """Create a strict prompt so the LLM only answers from context"""
        context_text = "\n\n".join(context)
        prompt = f"""You are an expert assistant. Answer ONLY using the context below. If the answer is not present in the context, reply: 'I cannot find this information in the provided documents.'
        
        Context:
        {context_text}
        
        Question: {query}
        
        Answer:"""
        return prompt
