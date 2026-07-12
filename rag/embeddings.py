import json
import os
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np 


#load documents
with open('rag/documents.json', 'r') as f:
    documents = json.load(f)

print(f"loaded {len(documents)} documents")

#load embedding model
print("loading embedding model...")
model = SentenceTransformer('all-MiniLM-L6-v2')

#convert documents to vectors
print("creating embeddings...")
embeddings = model.encode(documents, show_progress_bar=True)
print(f"embeddings shape: {embeddings.shape}")

# create FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings.astype(np.float32))

#save index
faiss.write_index(index, 'rag/faiss_index.bin')
print("FAISS index saved!")