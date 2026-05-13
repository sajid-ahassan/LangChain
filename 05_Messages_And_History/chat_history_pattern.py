"""
Revision goal: Simple chat history pattern.

For small apps, you can store messages in a list.
For bigger apps, use persistent storage such as Redis, database, or LangGraph persistence.
"""

from langchain_core.messages import HumanMessage, AIMessage

history = []

# User asks first question.
history.append(HumanMessage(content="What is LangChain?"))
history.append(AIMessage(content="A framework for building LLM applications."))

# User asks follow-up.
history.append(HumanMessage(content="What is it used for?"))

for msg in history:
    print(type(msg).__name__, msg.content)
