from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser 
from langchain.output_parsers import StructuredOutputParser , ResponseSchema

load_dotenv()

HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

print(os.getenv("HUGGINGFACEHUB_API_TOKEN"))


endpoint = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    huggingfacehub_api_token=HF_TOKEN,
    temperature=0.5
)

model = ChatHuggingFace(llm=endpoint)

parser = StructuredOutputParser()
schema = [
    ResponseSchema(name='fact_1',description='fact_1 is about the topic'),
    ResponseSchema(name='fact_2',description='fact_2 is about the topic'),
    ResponseSchema(name='fact_3',description='fact_3 is about the topic'),

]

template = PromptTemplate(
    template = "give 3 fact about {topic} \n {format_instruction}",
    input_variables = ['topic'],
    partial_variables= {'format_instruction':parser.get_format_instruction()}

)

prompt = template.invoke({'topic':'black hole'})
result = model.invoke(prompt)
final_reuslt = parser.parse(result.content)
print(final_reuslt)
