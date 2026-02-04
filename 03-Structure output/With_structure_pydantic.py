from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from pydantic import BaseModel,EmailStr , Field
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal
import os

load_dotenv()

HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

print(os.getenv("HUGGINGFACEHUB_API_TOKEN"))

# Pydantic clas
class review(TypedDict):
    summery :str = Field(description="A Brief summery of the review")
    sentiment: Literal['pos','neg'] = Field(description="Return the sentiment of the review")
    pros = Optional[list[str]] = Field(default=None,description="write the all pros")
    cons = Optional[list[str]] = Field(default=None,description="write the cons")



## ------------ Hugging Face model ------------
endpoint = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    huggingfacehub_api_token=HF_TOKEN,
    temperature=0.5
)

model = ChatHuggingFace(llm=endpoint)
structure_model = model.with_structured_output(review)

response = structure_model.invoke("I have been facing serious stability issues with GPT for the last 3 days. After logging in, the screen often appears blank and only shows the text input box. Even after typing, nothing happens and there is no response. Because of this problem, I am only able to use GPT in a private/incognito window. This issue is very frustrating and affects regular usage. I hope the team fixes this bug soon and improves the overall stability of the platform.")
print(response)
print(response['summery'])
print(response['sentiment'])

##  --------------- Chat GPT Model -------------------------

# chat_GPTmodel = ChatOpenAI()
# structured_model = chat_GPTmodel.with_structured_output(review)
# result = chat_GPTmodel.invoke("give any review")

# print(result)
# print(result['summery'])
# print(result['sentiment'])



## when we pass the with_structured_output --> behind the secne one prompot is generated and + out promopt pass on the model

## Huggingface is not work with the structureed output 