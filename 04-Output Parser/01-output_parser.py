from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate

load_dotenv()

HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

print(os.getenv("HUGGINGFACEHUB_API_TOKEN"))


endpoint = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    huggingfacehub_api_token=HF_TOKEN,
    temperature=0.5
)

model = ChatHuggingFace(llm=endpoint)

# 1st prompt --> detailed report
template1 = PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=['topic']
)

# 2nd prompt --> summery
template2 = PromptTemplate(
    template="write a 5 line summery on the following text./n{text}",
    input_variables=['text']
)

prompt1 = template1.invoke({'topic':'black hole'})

result = model.invoke(prompt1)

prompt2  = template2.invoke({'text':result.content})

result1 = model.invoke(prompt2) 
print(result1.content)