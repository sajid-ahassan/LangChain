"""
Revision goal: StrOutputParser.

Chat models return message objects. StrOutputParser extracts only the text.
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = ChatPromptTemplate.from_template("Give 3 bullet points about {topic}.")
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
parser = StrOutputParser()

# LCEL chain: output of prompt goes into model, then parser.
chain = prompt | model | parser

answer = chain.invoke({"topic": "LangChain output parsers"})
print(answer)
