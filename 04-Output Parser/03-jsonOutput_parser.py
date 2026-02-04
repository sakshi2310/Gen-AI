from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser

load_dotenv()

HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

print(os.getenv("HUGGINGFACEHUB_API_TOKEN"))


endpoint = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    huggingfacehub_api_token=HF_TOKEN,
    temperature=0.5
)

model = ChatHuggingFace(llm=endpoint)

parser= JsonOutputParser()
# 1st prompt --> detailed report
template1 = PromptTemplate(
    template="give me the name,age  and city of a fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()} # fil before the run time
)


# ---------------- Method 1 ---------------
# prompt = template1.format()
# print(prompt)
# result = model.invoke(prompt)
# print(result)
# final_result = parser.parse(result.content)
# print(final_result)
# print(type(final_result))
# print(final_result['name'])


# --------- Method 2 ----------------------
chain = template1 | model | parser
result = chain.invoke({}) # always send a dict in this 
print(result)
