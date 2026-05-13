"""
Revision goal: Message types.

SystemMessage: behavior/instructions.
HumanMessage: user input.
AIMessage: model response.
"""

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

messages = [
    SystemMessage(content="You are a strict but friendly tutor."),
    HumanMessage(content="What is a vector store?"),
    AIMessage(content="A vector store saves embeddings and searches by similarity."),
]

for message in messages:
    print(type(message).__name__, "->", message.content)
