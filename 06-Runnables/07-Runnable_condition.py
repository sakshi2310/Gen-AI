from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain_core.runnables import RunnableParallel ,RunnableBranch ,RunnableLambda,RunnableSequence,RunnablePassthrough

load_dotenv()

HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

print(os.getenv("HUGGINGFACEHUB_API_TOKEN"))


endpoint = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    huggingfacehub_api_token=HF_TOKEN,
    temperature=0.5
)

model = ChatHuggingFace(llm=endpoint)

prompt1 = PromptTemplate(
    template="write a detail report {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="summerize the following  {text}",
    input_variables=['text']
)


parser =StrOutputParser()

report_gen_chain =RunnableSequence(prompt1,model,parser)

branch_chain = RunnableBranch(
    (lambda x :len(x.split())>500,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()

)
final_chain = RunnableSequence(report_gen_chain,branch_chain)

print(final_chain.invoke({'topic':'Rassia Vs ukarian'}))