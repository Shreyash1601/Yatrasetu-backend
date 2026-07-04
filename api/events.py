from fastapi import APIRouter
from pydantic import BaseModel

from prompts.event_prompt import build_event_prompt
from services.gemini_service import gemini_service

router = APIRouter(prefix="/events", tags=["Events"])


class EventRequest(BaseModel):
    destination: str


@router.post("/")
def events(request: EventRequest):

    prompt = build_event_prompt(request.destination)

    return gemini_service.generate_json(prompt)