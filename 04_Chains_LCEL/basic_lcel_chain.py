"""
Revision goal: LCEL basics.

LCEL = LangChain Expression Language.
The pipe operator connects components: prompt | model | parser.
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = ChatPromptTemplate.from_template("Explain {concept} like I am 12.")
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
parser = StrOutputParser()

chain = prompt | model | parser

print(chain.invoke({"concept": "LCEL"}))
