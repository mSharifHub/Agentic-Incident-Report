import os
import time
import datetime
from langchain_core.tools import tool
from pydantic import ValidationError
from app.models import IncidentReport

@tool(args_schema=IncidentReport)
def submit_incident_report(**kwargs):
    """
    Call this ONLY when the user says 'Yes' to the summary.
    This tool validates completeness before saving.
    """
    try:
      
        report = IncidentReport(**kwargs)

        timestamp = int(time.time())
        filename = f"Incident_Report_{timestamp}.txt"
        filepath = os.path.join(".", filename)
    
        file_content = (
            f"INCIDENT REPORT #{timestamp}\n"
            f"========================================\n"
            f"REPORTING PARTY: {report.reporting_person.first_name} {report.reporting_person.last_name}\n"
            f"ADDRESS:         {report.reporting_person.address}\n"
            f"PHONE:           {report.reporting_person.phone}\n"
            f"----------------------------------------\n"
            f"LOCATION:        {report.where_location}\n"
            f"TIME:            {report.when_time}\n"
            f"----------------------------------------\n"
            f"NARRATIVE:\n{report.what_happened}\n"
            f"----------------------------------------\n"
            f"SUSPECT INFO:    {report.suspect_info.model_dump_json()}\n"
            f"VEHICLE INFO:    {report.vehicle_info.model_dump_json()}\n"
            f"========================================\n"
            f"STATUS: FILED"
        )

        with open(filepath, "w") as f:
            f.write(file_content)
        return f"Report saved to {filename}."

    except ValidationError as e:
        return f"DATA FORMAT ERROR: {str(e)}"
    except Exception as e:
        return f"SYSTEM ERROR: {str(e)}"

@tool
def calculate_date(relative_time: str) -> str:
    """
    Calculates the exact date based on a relative description (e.g., '2 days ago', 'last Friday').
    Always call this when the user gives a relative time.
    """
    today = datetime.date.today()
    relative_time = relative_time.lower()
    
    try:
        if "yesterday" in relative_time:
            target_date = today - datetime.timedelta(days=1)
        elif "ago" in relative_time and "day" in relative_time:
            # Extract number (e.g., "2 days ago")
            parts = relative_time.split()
            days = 1
            for part in parts:
                if part.isdigit():
                    days = int(part)
                    break
            target_date = today - datetime.timedelta(days=days)
        elif "week" in relative_time and "ago" in relative_time:
             target_date = today - datetime.timedelta(weeks=1)

        return target_date.strftime("%A, %B %d, %Y")
    except Exception:
        return f"Error calculating date. Today is {today.strftime('%A, %B %d, %Y')}."