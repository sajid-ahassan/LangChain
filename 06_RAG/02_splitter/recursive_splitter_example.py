"""
Revision goal: Text splitting.

RecursiveCharacterTextSplitter tries to split text using sensible boundaries:
paragraphs, then lines, then spaces, then characters.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

text = """
LangChain helps build LLM applications. RAG helps answer using documents.
Embeddings convert text into vectors. Vector stores search by similarity.
Retrievers fetch useful chunks for a query.
"""

docs = [Document(page_content=text, metadata={"source": "revision-note"})]

splitter = RecursiveCharacterTextSplitter(
    chunk_size=80,      # maximum characters per chunk
    chunk_overlap=15,   # repeated characters to preserve context
)

chunks = splitter.split_documents(docs)

for i, chunk in enumerate(chunks, start=1):
    print(f"--- Chunk {i} ---")
    print(chunk.page_content)
    print(chunk.metadata)
