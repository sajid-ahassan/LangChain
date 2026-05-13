"""
Revision goal: Agents.

An agent uses a model plus tools. It can decide which tool to call and when.
Modern LangChain uses create_agent for agent creation.
"""

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
load_dotenv()
model = ChatOpenAI(model = 'gpt-4o-mini')

@tool
def get_course_duration(course_name: str) -> str:
    """Return fake course duration for revision demo."""
    durations = {
        "langchain": "2 weeks for basics, 1 month for strong projects",
        "rag": "1 week for basics, 2 weeks with evaluation",
    }
    return durations.get(course_name.lower(), "Unknown duration")

agent = create_agent(
    model=model,
    tools=[get_course_duration],
    system_prompt="You are a helpful study planner.",
)

result = agent.invoke({
    "messages": [{"role": "user", "content": "How long should I revise LangChain?"}]
})

print(result)
