from fastapi import APIRouter
from pydantic import BaseModel

from prompts.culture_prompt import build_culture_prompt
from services.gemini_service import gemini_service

router = APIRouter(prefix="/culture", tags=["Culture"])


class CultureRequest(BaseModel):
    destination: str


@router.post("/")
def culture(request: CultureRequest):

    prompt = build_culture_prompt(request.destination)

    return {
        "culture": gemini_service.generate_text(prompt)
    }