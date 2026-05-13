# 00 - LangChain Map

## What LangChain is

LangChain is a framework for building applications around language models. It gives you reusable pieces for prompts, models, parsers, retrievers, tools, and agents.

## Main components

| Component | Meaning | Simple memory hook |
|---|---|---|
| Model | The LLM or embedding model | Brain |
| Prompt | Instructions sent to the model | Question paper |
| Chain | Connected steps | Pipeline |
| Output parser | Converts model output | Cleaner |
| Document loader | Reads source files/pages | Importer |
| Text splitter | Breaks documents into chunks | Cutter |
| Embeddings | Turns text into vectors | Meaning numbers |
| Vector store | Stores/searches vectors | Semantic database |
| Retriever | Finds relevant chunks | Searcher |
| Tool | Function the model can call | External ability |
| Agent | LLM that decides what to do next | Planner |
| Memory/history | Keeps conversation state | Notebook |

## The three most important flows

### 1. Simple LLM app

```text
User input -> PromptTemplate -> ChatModel -> OutputParser -> Final text
```

### 2. RAG app

```text
Raw docs -> Load -> Split -> Embed -> Store -> Retrieve -> Answer with context
```

### 3. Agent app

```text
User asks -> Model reasons -> Calls tool -> Reads result -> Answers
```

## Revision tip

When you forget LangChain, ask: what are my inputs, what model do I use, what context do I need, and what output shape do I want?
