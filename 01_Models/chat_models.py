"""
Revision goal: Understand chat models.

A chat model is the LLM that receives messages and returns an AI message.
Examples: ChatOpenAI, ChatAnthropic, ChatOllama, etc.
"""

from dotenv import load_dotenv

load_dotenv()  # Reads API keys from .env

# This import needs: pip install langchain-openai
from langchain_openai import ChatOpenAI

# temperature=0 means more deterministic answers.
# temperature closer to 1 means more creative/random answers.
model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
)

# invoke() is the basic call method in LangChain.
response = model.invoke("Explain LangChain in one sentence.")

# response is usually an AIMessage object.
print(response.content)
