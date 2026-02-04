from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser,PydanticOutputParser
from pydantic import BaseModel ,Field

load_dotenv()

HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

print(os.getenv("HUGGINGFACEHUB_API_TOKEN"))


endpoint = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    huggingfacehub_api_token=HF_TOKEN,
    temperature=0.5
)

model = ChatHuggingFace(llm=endpoint)

class person(BaseModel):
    name : str = Field(description="Name of the person")
    age : int = Field(gt=18,description="Age of the person")
    city : str = Field(description="Name of the city the person belongs to ")


parser  = PydanticOutputParser(pydantic_object=person)

template = PromptTemplate(
    template="generate the name , age and city of the fictional {place} person \n{format_instruction}",
    input_variables=['place'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

prompt = template.invoke({'place':'indian'})

result = model.invoke(prompt)
final_result = parser.parse(result.content)
print(final_result)