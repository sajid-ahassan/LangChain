"""
Revision goal: with_structured_output().

This asks the model to return data matching a Pydantic class.
The result becomes a normal Pydantic object, not raw text.
"""

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

load_dotenv()

class RevisionCard(BaseModel):
    topic: str = Field(description="Topic title")
    definition: str = Field(description="Simple definition")
    example: str = Field(description="Tiny example")

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
structured_model = model.with_structured_output(RevisionCard)

card = structured_model.invoke("Make a revision card for LangChain retrievers.")

print(card.topic)
print(card.definition)
print(card.example)
