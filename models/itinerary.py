from typing import List

from pydantic import BaseModel


class Activity(BaseModel):
    time: str
    title: str
    description: str


class DayPlan(BaseModel):
    day: int
    activities: List[Activity]


class ItineraryResponse(BaseModel):
    title: str
    days: List[DayPlan]