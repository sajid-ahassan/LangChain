"""
Revision goal: Tools.

A tool is a Python function that a model/agent can call.
Use tools when the model needs an external ability: calculator, search, database, API.
"""

from langchain_core.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b

print(multiply.name)
print(multiply.description)
print(multiply.invoke({"a": 6, "b": 7}))
