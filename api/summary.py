from fastapi import APIRouter

from models.destination import DestinationRequest
from prompts.summary_prompt import build_summary_prompt
from services.gemini_service import gemini_service

router = APIRouter(
    prefix="/summary",
    tags=["Summary"]
)


@router.post("/")
def summary(request: DestinationRequest):

    prompt = build_summary_prompt(
        request.destination,
        request.days,
        request.budget,
        request.interests
    )

    return {
        "summary": gemini_service.generate_text(prompt)
    }