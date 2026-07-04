from typing import List

from pydantic import BaseModel


class UserPreferences(BaseModel):
    interests: List[str] = []
    travel_style: str = "balanced"