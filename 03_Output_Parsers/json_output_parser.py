"""
Revision goal: JsonOutputParser.

Use JSON parsing when you want a dictionary-like output.
Note: For strict production apps, Pydantic structured output is usually safer.
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

parser = JsonOutputParser()

prompt = ChatPromptTemplate.from_template(
    "Return a JSON object with keys: topic, definition, example. Topic: {topic}"
)

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
chain = prompt | model | parser

result = chain.invoke({"topic": "embedding"})
print(result)
print(result["definition"])
