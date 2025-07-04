from pydantic import BaseModel
class GoalInput(BaseModel):
    """GoalInput model definition"""
    goal_type : str 
    quantity : float
    metric : str
    duration : str 

class MealPlanOutput(BaseModel):
    meals : list[str]

class WorkoutPlanOutput(BaseModel):
    plan : dict