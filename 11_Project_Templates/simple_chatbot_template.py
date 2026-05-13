"""
Simple chatbot template.

Use this when you only need prompt + model + parser.
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{input}"),
])

chain = prompt | ChatOpenAI(model="gpt-4o-mini") | StrOutputParser()

print(chain.invoke({"input": "Give me a study tip."}))
