# RAG Evaluation Checklist

Use this when your RAG answer is bad.

## Retrieval checks

- Are the right documents loaded?
- Are chunks too large or too small?
- Is chunk overlap enough?
- Is metadata preserved?
- Is top-k too low or too high?
- Are retrieved chunks actually relevant?

## Generation checks

- Does the prompt say to answer only from context?
- Does the prompt ask the model to say "I don't know" when context is missing?
- Is the context formatted clearly?
- Is the model temperature low for factual QA?

## Debugging print statements

Always print retrieved chunks before blaming the model.

```python
for doc in retrieved_docs:
    print(doc.page_content)
    print(doc.metadata)
```

## Common failure patterns

| Problem | Likely cause |
|---|---|
| Hallucination | Prompt too loose or no relevant context |
| Missing answer | Bad retrieval or bad chunking |
| Confused answer | Too many unrelated chunks |
| Slow app | Large docs, expensive model, no caching |
| No source citation | Metadata not preserved |
