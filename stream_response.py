from langchain_community.llms import Ollama

# Initialize the Ollama model
llm = Ollama(model="llama3")

# Stream the response chunks
for chunk in llm.stream("Tell me a short story about a robot."):
    print(chunk, end="", flush=True)
