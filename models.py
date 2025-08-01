from pydantic import BaseModel

class UserInterest(BaseModel):
    interests: list[str]
    current_skills: list[str] = []
    education_level: str | None = None

class CareerSuggestion(BaseModel):
    career: str
    match_score: float

class SkillRoadmap(BaseModel):
    skills: list[str]
    learning_path: list[str]