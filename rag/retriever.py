import numpy as np 
import json 
import os
from sentence_transformers import SentenceTransformer
import faiss

#load everything 
with open('rag/documents.json', 'r') as f:
    documents = json.load(f)

index = faiss.read_index('rag/faiss_index.bin')
model = SentenceTransformer('all-MiniLM-L6-v2')

def retrieve(query, top_k=5):
    #convert question to vector
    query_vector = model.encode([query]).astype(np.float32)

    #search FAISS for similar documents
    distances, indices = index.search(query_vector, top_k)

    #return matching documents 
    results = [documents[i] for i in indices[0]]
    return results

#test it 
query = "Which products are in warehouse B?"
results = retrieve(query)
print(f"Query: {query}\n")
for i, result in enumerate(results):
    print(f"Result {i+1}:{result}")