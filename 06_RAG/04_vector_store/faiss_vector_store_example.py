"""
Revision goal: Vector stores.

A vector store saves embedded chunks and lets you search similar chunks.
This example uses FAISS, a local vector store.
Requires: pip install faiss-cpu langchain-community langchain-openai
"""

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

load_dotenv()

texts = [
    Document(page_content="LangChain connects prompts, models, and parsers.", metadata={"topic": "basics"}),
    Document(page_content="RAG retrieves relevant context before answering.", metadata={"topic": "rag"}),
    Document(page_content="Agents can use tools to complete tasks.", metadata={"topic": "agents"}),
]

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# from_documents embeds documents and stores them.
vector_store = FAISS.from_documents(texts, embeddings)

results = vector_store.similarity_search("How does retrieval help?", k=2)

for doc in results:
    print(doc.page_content)
    print(doc.metadata)
