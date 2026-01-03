# Agentic Incident Reporter 

> **Status**: Under Development 

An AI-powered administrative intake agent designed to securely and strictly document incident reports. Built with **LangGraph** and **LangChain**, this agent acts as a "Documentation System" rather than a chatbot, strictly following an interview protocol to validate user identity, location, and timelines before filing a report.

##  Key Features

* ** Strict Protocol Enforcement**: The agent refuses to move to the next interview phase until specific data points (e.g., Last Name, Exact Address) are collected.

* ** Dynamic Context Awareness**: Automatically calculates relative dates (e.g., converts "2 days ago" to "Wednesday, January 1st, 2026") using custom tools.

* ** Structured Output**: Validates all data against Pydantic schemas before saving final reports as standardized text files.

##  Tech Stack

* **Python 3.13+**
* **Orchestration**: LangChain, LangGraph (Stateful Multi-Turn Agents)
* **LLM**: OpenAI GPT-4o (Configurable)
* **Validation**: Pydantic
* **Package Manager**: uv

##  Project Structure

```text
incident_bot/
├── app/
│   ├── agents/
│   │   └── intaker_agent.py    # Main graph logic & system prompts
│   ├── models.py               # Pydantic data schemas
│   └── tools.py                # Tools for Date, Address, and File Saving
├── main.py                     # CLI Entry point
├── .env                        # API Keys (Not committed)
├── pyproject.toml              # Dependencies (uv)
└── README.md
```

##  Installation

Ensure you have [uv](https://github.com/astral-sh/uv) installed.

```bash
# Clone the repository
git clone [https://github.com/yourusername/Agentic-Incident-Report.git](https://github.com/yourusername/Agentic-Incident-Report.git)
cd Agentic-Incident-Report

# Create virtual environment and sync dependencies
uv sync
