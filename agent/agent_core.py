import os
import json
import numpy as np
from dotenv import load_dotenv
from groq import Groq
import faiss
from sentence_transformers import SentenceTransformer

load_dotenv()

# Configure Groq
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

print("API Key loaded:", os.getenv('GROQ_API_KEY')[:10])



#load RAG components
with open('rag/documents.json', 'r') as f:
    documents = json.load(f)

index = faiss.read_index('rag/faiss_index.bin')
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

print("All components loaded successfully")

def ask_agent(question):

    question_vector = embedding_model.encode([question]).astype(np.float32)

    distances, indices = index.search(question_vector, 15)
    relevant_docs = [documents[i] for i in indices[0]]
    context = "\n".join(relevant_docs)

    #build prompt for gemini 
    prompt = f""" 
    you are a smart inventory management assistant.
    use the following inventory data to answer the question.

    Inventory Data:
    {context}

    Question: {question}

    Give a clear, concise business answer.
    
    """

    response = client.chat.completions.create(
    model='llama-3.3-70b-versatile',
    messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

    return response.text
print(ask_agent("Which products are expiring soon in warehouse B? "))

