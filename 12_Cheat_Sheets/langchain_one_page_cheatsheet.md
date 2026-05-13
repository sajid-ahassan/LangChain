# LangChain One Page Cheat Sheet

## Model

```python
model.invoke("Hello")
```

## Prompt

```python
prompt = ChatPromptTemplate.from_template("Explain {topic}")
prompt.invoke({"topic": "RAG"})
```

## Chain

```python
chain = prompt | model | parser
chain.invoke({"topic": "RAG"})
```

## RAG

```python
retriever = vector_store.as_retriever(search_kwargs={"k": 3})
```

## Structured output

```python
structured_model = model.with_structured_output(MySchema)
```

## Tool

```python
@tool
def search(query: str) -> str:
    """Search something."""
    return "result"
```

## Agent

```python
agent = create_agent(model="openai:gpt-4o-mini", tools=[tool])
```

## Most common imports

```python
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document
from langchain_core.tools import tool
from langchain_text_splitters import RecursiveCharacterTextSplitter
```
