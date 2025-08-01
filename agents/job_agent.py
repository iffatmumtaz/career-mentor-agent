from ..agents.llm_agent import generate_text 
import json
from typing import List, Dict

def get_job_roles(career: str) -> List[Dict[str, str]]:
    """Get real-world job roles for a specific career"""
    prompt = f"""
    Provide 3 real job roles for: {career}
    Include for each:
    - Title
    - Salary range
    - Key responsibilities
    
    Return as JSON format:
    {{
      "jobs": [
        {{
          "title": "Job Title",
          "salary": "$XXXK",
          "responsibilities": ["task1", "task2"]
        }}
      ]
    }}
    """
    
    if response := generate_text(prompt):
        try:
            data = json.loads(response)
            return data.get("jobs", [])
        except (json.JSONDecodeError, KeyError):
            pass
    return [] 