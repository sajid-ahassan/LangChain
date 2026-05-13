# Embeddings in RAG

An embedding is a list of numbers that represents the meaning of text.

Example idea:

```text
"dog" and "puppy" -> nearby vectors
"dog" and "database" -> far vectors
```

In RAG:

1. Embed every document chunk.
2. Store the vectors.
3. Embed the user question.
4. Search for chunks with similar vectors.

## Important terms

- Vector: numeric representation of text.
- Similarity: how close two vectors are.
- Top-k: number of chunks retrieved.
- Metadata: source/page information attached to chunks.
