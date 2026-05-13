"""
Revision goal: Passing history manually.

This is the easiest way to understand memory before using advanced storage.
"""

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer based on the conversation history."),
    MessagesPlaceholder("history"),
    ("human", "{input}"),
])

history = [
    HumanMessage(content="My favorite topic is RAG."),
    AIMessage(content="Got it. RAG is your favorite topic."),
]

formatted = prompt.invoke({
    "history": history,
    "input": "What is my favorite topic?",
})

print(formatted)
