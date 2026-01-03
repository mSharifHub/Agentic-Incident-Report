
import uuid
from dotenv import load_dotenv
load_dotenv() 
from app.agents import intaker_agent

def run_cli():

    config = {"configurable": {"thread_id": str(uuid.uuid4())}}

    while True:
        try:
            user_input = input("\nReportee: ")
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            break

        if user_input.lower() in ["exit", "done", "quit"]:
            break

        if not user_input.strip():
            continue

        for step in intaker_agent.stream(
            {"messages": [{"role": "user", "content": user_input}]},
            config=config,
            stream_mode="values"
        ):
            last_message = step["messages"][-1]

            if last_message.type == "ai" and last_message.content:
                print(f"Agent: {last_message.content}")

        
            if last_message.type == "tool":
                print(f"\n[System Validator]: {last_message.content}")
            
    


if __name__ == "__main__":
    run_cli()
