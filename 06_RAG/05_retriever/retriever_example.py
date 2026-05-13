"""
Revision goal: Retriever.

A retriever is a standard interface that returns relevant documents for a query.
Vector stores can usually be converted into retrievers with as_retriever().
"""

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

load_dotenv()

texts = [
    Document(page_content="Prompt templates format user input for models."),
    Document(page_content="Text splitters break documents into chunks."),
    Document(page_content="Retrievers return relevant chunks for a question."),
]

vector_store = FAISS.from_documents(texts, OpenAIEmbeddings(model="text-embedding-3-small"))

retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}  # return top 2 chunks
)

retrieved_docs = retriever.invoke("What finds relevant chunks?")

for doc in retrieved_docs:
    print(doc.page_content)
