from typing import List, Optional

from pydantic import BaseModel, Field


class DestinationRequest(BaseModel):
    destination: str = Field(..., example="Jaipur")
    days: int = Field(default=2, ge=1)
    budget: Optional[int] = Field(default=None, example=5000)
    interests: List[str] = Field(
        default_factory=list,
        example=["history", "food", "culture"]
    )