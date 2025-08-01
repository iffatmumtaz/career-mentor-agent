import json
from typing import List
from  models import UserInterest, CareerSuggestion
from .llm_agent import generate_text 

def suggest_careers(user: UserInterest) -> List[CareerSuggestion]:
    """Get career suggestions based on user profile"""
    prompt = f"""
    Suggest 3 careers for:
    Interests: {user.interests}
    Skills: {user.current_skills}
    Education: {user.education_level}
    
    Return JSON format:
    {{"careers": [{{"name": "Career", "score": 0.9}}]}}
    """
    
    if response := generate_text(prompt):
        try:
            data = json.loads(response)
            return [
                CareerSuggestion(career=item["name"], match_score=item["score"])
                for item in data.get("careers", [])
            ]
        except (json.JSONDecodeError, KeyError):
            pass
    return []