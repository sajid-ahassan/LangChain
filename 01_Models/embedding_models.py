"""
Revision goal: Understand embedding models.

Embedding models convert text into vectors. Similar meaning = nearby vectors.
Embeddings are used heavily in RAG and semantic search.
"""

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# embed_query() embeds a single string.
vector = embeddings.embed_query("LangChain helps build LLM apps")

print(type(vector))      # list
print(len(vector))       # vector dimension depends on the embedding model
print(vector[:5])        # first few numbers only
