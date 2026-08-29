from langchain_ollama import OllamaEmbeddings

# Initialize the embedding engine
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# Embed a single query or a batch of documents
query_vector = embeddings.embed_query("What is LangChain?")
doc_vectors = embeddings.embed_documents(["Doc 1 text", "Doc 2 text"])

print(f"Embedding dimensions: {len(query_vector)}")
