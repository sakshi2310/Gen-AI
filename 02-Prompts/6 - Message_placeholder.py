from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

chat_template = ChatPromptTemplate(
    messages=[
        ("system", "You are a helpful customer support agent"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{query}")
    ]
)


# Load chat history

file_path = r"D:\Gen AI Campasx\Prompts\6.1-chat_history.txt"


chat_history = []
with open(file_path,  'r') as f:
    chat_history.extend(f.readlines())

print(chat_history)

# Create prompt

prmot = chat_template.invoke({'chat_history':chat_history,'query':'where is my refund'})

print(prmot)