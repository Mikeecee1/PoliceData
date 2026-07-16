from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

# set file path
path = os.path.dirname(os.path.realpath(__file__))
path+= "/data/"

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# list files in data folder
files = os.listdir(path)

# The sentences to encode
sentences = []

for f in files:
    file_path = path + f
    with open(file_path, 'r') as file:
        sentences+= [line.strip() for line in file]

# print(sentences)


# 2. Calculate embeddings by calling model.encode()
embeddings = model.encode(sentences)

# Create FAISS index
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

# Add embeddings into the index
index.add(np.array(embeddings))

# -----------------------------
# QUERY SECTION
# -----------------------------
run_query = True

while run_query:
    user_query = input("Enter your query or type x to stop: ")

    if user_query.lower() == "x":
        run_query = False
    else:
        query = model.encode([user_query])

        D, I = index.search(np.array(query), k=1)

        for i in I[0]:
            print(sentences[i])