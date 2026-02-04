from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()


emb = OpenAIEmbeddings(modeel="",dimentions=32)
result = emb.enbed_query("What is capital of india")

print(str(result))