# RAG Project Template

```text
project/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── loaders.py
│   ├── splitters.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── prompts.py
│   ├── chains.py
│   └── app.py
├── tests/
├── .env
├── requirements.txt
└── README.md
```

## File responsibilities

- `loaders.py`: read PDFs, text files, web pages, etc.
- `splitters.py`: chunk documents.
- `embeddings.py`: create embedding model.
- `vector_store.py`: create/load vector database.
- `retriever.py`: configure retrieval strategy.
- `prompts.py`: store prompt templates.
- `chains.py`: connect retriever, prompt, model, parser.
- `app.py`: user interface or API entry point.
