"""
Revision goal: Tool calling.

A tool-calling model can decide to call tools based on the user request.
This shows binding tools to a chat model.
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

load_dotenv()

@tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
model_with_tools = model.bind_tools([add])

response = model_with_tools.invoke("What is 15 + 27? Use the tool.")

# If the model decides to call a tool, tool calls appear here.
print(response.tool_calls)
