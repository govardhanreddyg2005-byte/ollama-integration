from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

chat = ChatOllama(model="llama3.1", temperature=0.3)

messages = [
    SystemMessage(content="You are a helpful coding assistant."),
    HumanMessage(content="How do I reverse a list in Python?")
]

response = chat.invoke(messages)
print(response.content)
