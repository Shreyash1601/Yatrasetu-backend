from fastapi import APIRouter
from pydantic import BaseModel

from prompts.hidden_prompt import build_hidden_prompt
from services.gemini_service import gemini_service

router = APIRouter(prefix="/hidden-gems", tags=["Hidden Gems"])


class HiddenGemRequest(BaseModel):
    destination: str


@router.post("/")
def hidden_gems(request: HiddenGemRequest):

    prompt = build_hidden_prompt(request.destination)

    return gemini_service.generate_json(prompt)