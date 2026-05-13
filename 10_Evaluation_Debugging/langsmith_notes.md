# LangSmith Notes

LangSmith is useful for tracing, debugging, and evaluating LangChain applications.

## Why use it?

- See every step in your chain.
- Inspect prompt inputs and model outputs.
- Debug retrieval quality.
- Compare runs during evaluation.

## Environment variables commonly used

```bash
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your_key_here
LANGSMITH_PROJECT=langchain-revision
```

## Mental hook

LangChain builds the app. LangSmith helps you see what happened inside the app.
