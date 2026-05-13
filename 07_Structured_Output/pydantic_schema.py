"""
Revision goal: Pydantic schema.

A schema defines the exact shape you want back from the model.
This is useful for extraction, classification, routing, and APIs.
"""

from pydantic import BaseModel, Field

class TopicSummary(BaseModel):
    # Field description helps the model understand what to return.
    topic: str = Field(description="Main topic name")
    short_definition: str = Field(description="One sentence definition")
    difficulty: str = Field(description="easy, medium, or hard")
    keywords: list[str] = Field(description="Important keywords")

print(TopicSummary.model_json_schema())
