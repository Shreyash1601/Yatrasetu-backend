from fastapi import APIRouter
from pydantic import BaseModel

from prompts.storyteller_prompt import build_story_prompt
from services.gemini_service import gemini_service

router = APIRouter(prefix="/story", tags=["Story"])


class StoryRequest(BaseModel):
    place: str
    style: str = "historian"


@router.post("/")
def generate_story(request: StoryRequest):

    prompt = build_story_prompt(
        request.place,
        request.style
    )

    return {
        "story": gemini_service.generate_text(prompt)
    }