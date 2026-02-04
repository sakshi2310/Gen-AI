
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain_core.runnables import RunnableParallel ,RunnableBranch ,RunnableLambda
from pydantic import BaseModel,Field 
from typing import Literal

load_dotenv()

HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

print(os.getenv("HUGGINGFACEHUB_API_TOKEN"))


endpoint = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    huggingfacehub_api_token=HF_TOKEN,
    temperature=0.5
)

model = ChatHuggingFace(llm=endpoint)

class Feedback(BaseModel):
    sentiment : Literal['positive','negative'] = Field(description="Give the sentiment of the Feedback")



parser = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n{format_instruction}",
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}

)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template="Write an appropriate responsse to this positive feedback \n {feedback}",
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template="Write an appropriate responsse to this Negative feedback \n {feedback}",
    input_variables=['feedback']
)

brach_chain = RunnableBranch(
    (lambda x : x.sentiment == "positive",prompt2|model|parser),
    (lambda x: x.sentiment == "negative",prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not find the sentiment") # here this is not chain so we need to convert it into the runnable
)

chain = classifier_chain | brach_chain

result = chain.invoke({'feedback':'too many ads!!'})
print(result)







