# LangChain Revision Material

This folder is designed for revision: open the folders in order and read the comments inside the code files. Every file is intentionally small, focused, and easy to scan.

## Best revision order

1. `01_Models` - chat models and embedding models.
2. `02_Prompts` - prompt templates, chat prompts, placeholders.
4. `03_Output_Parsers` - turning model text into clean Python values.
5. `04_Chains_LCEL` - the pipe style: `prompt | model | parser`.
6. `05_Messages_And_History` - system/user/AI messages and chat history.
7. `06_RAG` - loader, splitter, embeddings, vector store, retriever, generation.
8. `07_Structured_Output` - Pydantic schemas and JSON-like responses.
9. `08_Tools_And_Agents` - tools, tool calling, agents.
10. `09_Memory` - short-term and long-term conversation memory ideas.

## Core mental model

LangChain helps you connect these blocks:

```text
Input -> Prompt -> Model -> Parser -> Output
```

For RAG:

```text
Documents -> Loader -> Splitter -> Embeddings -> Vector Store -> Retriever -> Prompt -> Model -> Answer
```

For agents:

```text
User goal -> Agent/LLM decides -> Tool call -> Observation -> Final answer
```

## Install notes

LangChain is modular. Common packages:

```bash
pip install langchain langchain-core langchain-community langchain-openai langchain-text-splitters python-dotenv pydantic
```

Optional for local vector store examples:

```bash
pip install faiss-cpu chromadb
```

Create a `.env` file when using real APIs:

```bash
OPENAI_API_KEY=your_key_here
```

Most code files are revision snippets. Some need an API key or optional packages before running.
