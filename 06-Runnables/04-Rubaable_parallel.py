from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain_core.runnables import RunnableParallel ,RunnableBranch ,RunnableLambda,RunnableSequence

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
    template="Generate a tweet about the {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Generate the linked aboth the {topic}",
    input_variables=['topic']
)
parser =StrOutputParser()

parallel_chian = RunnableParallel({
    'tweet':RunnableSequence(prompt1,model,parser),
    'linkding' :RunnableSequence(prompt2,model,parser)
})
print(parallel_chian.invoke({'topic':'AI'}))