# RAG Revision Flow

RAG = Retrieval Augmented Generation.

Instead of asking the model to answer from memory only, RAG gives it relevant context from your documents.

## Pipeline

```text
1. Load documents
2. Split documents into chunks
3. Convert chunks to embeddings
4. Store embeddings in vector store
5. Retrieve relevant chunks for a question
6. Put chunks into prompt context
7. Generate answer with the LLM
```

## Why split documents?

Large documents cannot fit into the model context easily. Splitting creates smaller searchable chunks.

## Why embeddings?

Embeddings allow semantic search. The query and documents are compared by meaning, not exact words only.

## Why retrievers?

A retriever is a clean interface that says: for this query, return relevant documents.

## RAG quality depends on

- chunk size
- chunk overlap
- embedding model
- vector store
- retrieval strategy
- prompt quality
- evaluation
