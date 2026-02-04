from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage , AIMessage , HumanMessage

# chat_template = ChatPromptTemplate([
#     SystemMessage(content="You are helpful {domain} expert"),
#     HumanMessage(content='Explaing in simple terms , what is {topic}')
# ])

chat_template = ChatPromptTemplate(
    ('system','You are helpful {domain} expert'),
    ('human','Explaing in simple terms , what is {topic}')
)

prompt = chat_template.invoke({'domain':'Cricket','topic':'Durse'})

print(prompt)