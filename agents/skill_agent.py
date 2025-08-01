from ..tools.roadmap_tool import get_career_roadmap
from ..models import SkillRoadmap

def generate_roadmap(career: str) -> SkillRoadmap:
    """Generate skill roadmap for a specific career"""
    return SkillRoadmap(**get_career_roadmap(career))