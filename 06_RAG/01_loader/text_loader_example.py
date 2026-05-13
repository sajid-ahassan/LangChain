"""
Revision goal: Document loaders.

Loaders convert files/web pages/databases into LangChain Document objects.
Each Document has:
- page_content: the text
- metadata: source, page number, etc.
"""

from langchain_community.document_loaders import TextLoader

loader = TextLoader("sample_data/langchain_notes.txt", encoding="utf-8")
docs = loader.load()

print(type(docs[0]))
print(docs[0].page_content[:100])
print(docs[0].metadata)
