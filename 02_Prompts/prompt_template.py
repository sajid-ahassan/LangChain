"""
Revision goal: PromptTemplate.

PromptTemplate is for normal string prompts with variables.
Use it when your prompt is not a chat-style message list.
"""

from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    "Explain {topic} in a {style} way. Keep it under {words} words."
)

# format() fills the placeholders.
formatted_prompt = prompt.format(
    topic="RAG",
    style="beginner-friendly",
    words=50,
)

print(formatted_prompt)
