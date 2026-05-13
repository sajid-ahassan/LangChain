"""
Revision goal: Complete small RAG chain.

This file shows the full flow:
Documents -> VectorStore -> Retriever -> Prompt -> Model -> Parser
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

# 1. Prepare tiny documents.
docs = [
    Document(page_content="LangChain uses LCEL to connect components with pipe syntax."),
    Document(page_content="RAG retrieves relevant context and passes it to the model."),
    Document(page_content="Structured output makes models return predictable data shapes."),
]

# 2. Create vector store.
vector_store = FAISS.from_documents(docs, OpenAIEmbeddings(model="text-embedding-3-small"))

# 3. Convert vector store to retriever.
retriever = vector_store.as_retriever(search_kwargs={"k": 2})

# 4. Format retrieved documents into one context string.
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# 5. Prompt uses both context and question.
prompt = ChatPromptTemplate.from_template(
    """
Answer using only the context below.

Context:
{context}

Question: {question}
"""
)

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
parser = StrOutputParser()

# RunnablePassthrough keeps the original question.
rag_chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough(),
    }
    | prompt
    | model
    | parser
)

answer = rag_chain.invoke("What does RAG do?")
print(answer)
