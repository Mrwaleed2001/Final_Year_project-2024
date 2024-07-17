import pandas as pd
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer

# Load the DataFrame
df = pd.read_csv('preprocessed_data.csv')

# Initialize the model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Dictionary to store embeddings
embeddings_dict = {}

# Iterate through each column in the DataFrame
for column in df.columns:
    texts = df[column].astype(str).tolist()  
    embeddings = model.encode(texts)  
    embeddings_dict[column] = embeddings  

# Save embeddings to a file
with open('all_embeddings.pkl', 'wb') as f:
    pickle.dump(embeddings_dict, f)

print("Embeddings created and stored successfully.")

# Load embeddings from the file
with open('all_embeddings.pkl', 'rb') as f:
    embeddings_dict = pickle.load(f)

# Example: Access embeddings for a specific column
column_name = 'EI1'  
column_embeddings = embeddings_dict.get(column_name)

print(column_embeddings)
print(len(column_embeddings))

from langchain_huggingface import HuggingFaceEmbeddings

embeddings_model = HuggingFaceEmbeddings()

embeddings_dict = {}

# # Load the DataFrame
df = pd.read_csv('preprocessed_data.csv')


# # Iterate through each column in the DataFrame
for column in df.columns:
    texts = df[column].astype(str).tolist()  
    embeddings = embeddings_model.embed_documents(texts)  
    embeddings_dict[column] = embeddings  

# Save embeddings to a file
with open('all_embeddings_hugging_face.pkl', 'wb') as f:
    pickle.dump(embeddings_dict, f)

print("Embeddings created and stored successfully.")

# Load embeddings from the file
with open('all_embeddings_hugging_face.pkl', 'rb') as f:
    embeddings_dict = pickle.load(f)

# Example: Access embeddings for a specific column
column_name = 'EI1'  
column_embeddings = embeddings_dict.get(column_name)

print(len(column_embeddings))
print(len(column_embeddings[0]))



