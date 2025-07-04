from pydantic import BaseModel
from typing import Optional , List , Dict

class UserSessionContext(BaseModel):
    name : str
    id : int
    goal : Optional[dict] = None
    diet_preferences : Optional[dict] = None
    meal_plain : Optional[dict] = None
    injury_notes: Optional[dict]=None
    handoff_logs: List[str] = []
    progress_logs : List[Dict[str , str]] = []