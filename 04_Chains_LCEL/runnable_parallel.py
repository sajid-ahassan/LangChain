"""
Revision goal: RunnableParallel.

RunnableParallel runs multiple chains on the same input and returns a dictionary.
Useful for generating multiple views at once.
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
parser = StrOutputParser()

summary_chain = ChatPromptTemplate.from_template("Summarize {topic} in 2 lines.") | model | parser
quiz_chain = ChatPromptTemplate.from_template("Make 3 quiz questions about {topic}.") | model | parser

parallel = RunnableParallel(
    summary=summary_chain,
    quiz=quiz_chain,
)
combine_prompt = ChatPromptTemplate.from_messages([
    ('system',"combine summary and quiz"),
    ('human',"summary : {summary}\nquiz : {quiz}")
])

combine_chain = parallel | combine_prompt | model | parser

result = combine_chain.invoke({"topic": "RAG"})

print(result)
