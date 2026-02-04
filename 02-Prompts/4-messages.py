from langchain_core.messages import SystemMessage , HumanMessage ,AIMessage
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
import os

load_dotenv()
HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

endpoint = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    huggingfacehub_api_token=HF_TOKEN,
    temperature=0.5
)

chat = ChatHuggingFace(llm=endpoint)

messages = [
    SystemMessage(content="You are a helpful assitant"),
    HumanMessage(content="Tell me about the langchain")
]

result = chat.invoke(messages)

messages.append(AIMessage(content=result.content))
print(messages)