"""
Revision goal: Debug retrieval.

Before improving prompts, inspect what your retriever returns.
Bad context usually means bad answer.
"""

def debug_docs(docs):
    for i, doc in enumerate(docs, start=1):
        print(f"\n--- Retrieved doc {i} ---")
        print("Content:", doc.page_content[:500])
        print("Metadata:", doc.metadata)

# Example usage after retrieval:
# retrieved_docs = retriever.invoke("your question")
# debug_docs(retrieved_docs)
