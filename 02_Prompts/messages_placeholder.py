"""
Revision goal: MessagesPlaceholder.

Use MessagesPlaceholder when you want to insert previous conversation history
into a new prompt.
"""

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}"),
])

history = [
    HumanMessage(content="What is RAG?"),
    AIMessage(content="RAG means retrieval augmented generation."),
]

result = prompt.invoke({
    "history": history,
    "question": "Why does it reduce hallucination?",
})

print(result)
