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
    template="write a funny joke about {topic}",
    input_variables=['topic']
)


parser =StrOutputParser()

joke_gen = RunnableSequence(prompt1,model,parser)

def word_count(text):
    return len(text.split())

parallel_chain =  RunnableParallel({
    'joke': RunnablePassthrough(),
    'wordcount':RunnableLambda(word_count),
    # 'wordcount': RunnableLambda(lambda x : len(x.split()))  # its is another way to define the lamda funtion
})

final_chain = RunnableSequence(joke_gen,parallel_chain)

print(final_chain.invoke({'topic':'AI'}))