from langchain_openai import OpenAIEmbeddings
import numpy as np
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimension=300)
documents = [
    "virat kohli is creicketer",
    "arman malik is singer",
    "anushka sen is preety"
]

query = 'tell me about virat kohli'

doc_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity(([query_embedding],doc_embedding))[0] # always pass 2d list

print(sorted(list(enumerate(scores)),key=lambda x:x[1]))

index , scores = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("Similarity score is :",scores)
