from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.messages import SystemMessage , AIMessage , HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

print(os.getenv("HUGGINGFACEHUB_API_TOKEN"))


endpoint = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    huggingfacehub_api_token=HF_TOKEN,
    temperature=0.5
)

chat = ChatHuggingFace(llm=endpoint)

chat_history = [
    SystemMessage(content="You are a Helpful assistant")
]

while True:
    user_input = input("You:")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    result = chat.invoke(chat_history)
    print("AI :",result.content)
    chat_history.append(AIMessage(content=result.content))
    print(chat_history)

