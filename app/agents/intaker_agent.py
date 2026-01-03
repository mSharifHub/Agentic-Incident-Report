from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
from app.tools import submit_incident_report, calculate_date
from app.report_intaker_system_prompt import system_prompt


model = ChatOpenAI(model="gpt-4o", temperature=1)

checkPointer = InMemorySaver()

agent = create_agent(
    model,
    tools=[submit_incident_report,calculate_date],
    system_prompt=system_prompt,
    checkpointer=checkPointer
)