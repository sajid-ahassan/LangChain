"""
Revision goal: ChatPromptTemplate.

ChatPromptTemplate creates a list of chat messages: system, human, AI, etc.
This is usually better for chat models.
"""

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful LangChain tutor."),
    ("human", "Explain {topic} with a tiny example."),
    # ("ai", "Explain {topic} with a tiny example."),
])

messages = prompt.invoke({"topic": "retrievers"})

# messages is a ChatPromptValue containing formatted messages.
print(messages)


