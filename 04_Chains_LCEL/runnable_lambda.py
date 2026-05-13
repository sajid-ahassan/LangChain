"""
Revision goal: RunnableLambda.

RunnableLambda lets you insert normal Python functions inside LCEL chains.
"""

from langchain_core.runnables import RunnableLambda

# Normal Python function.
def add_prefix(text: str) -> str:
    return "Revision note: " + text

chain = RunnableLambda(add_prefix)

print(chain.invoke("LCEL connects components."))
