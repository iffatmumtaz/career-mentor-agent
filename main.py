from fastapi import FastAPI
from models import UserInterest
from agents.career_agent import suggest_careers
from agents.skill_agent import generate_roadmap
from agents.job_agent import get_job_roles

app = FastAPI()

@app.post("/career-guide")
def career_guide(user: UserInterest):
    """Endpoint that combines career suggestions, skill roadmap and job info"""
    # Step 1: Get career suggestions
    careers = suggest_careers(user)
    
    if not careers:
        return {"error": "No career suggestions found"}
    
    # Step 2: Get roadmap for first suggested career
    roadmap = generate_roadmap(careers[0].career)
    
    # Step 3: Get job roles for first suggested career
    jobs = get_job_roles(careers[0].career)
    
    return {
        "suggested_careers": [c.model_dump() for c in careers],
        "roadmap": roadmap.model_dump() if roadmap else None,
        "job_roles": jobs
    }