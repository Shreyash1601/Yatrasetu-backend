from fastapi import APIRouter

from models.destination import DestinationRequest
from prompts.itinerary_prompt import build_itinerary_prompt
from services.gemini_service import gemini_service

router = APIRouter(prefix="/itinerary", tags=["Itinerary"])


@router.post("/")
def generate_itinerary(request: DestinationRequest):

    prompt = build_itinerary_prompt(
        request.destination,
        request.days,
        request.budget,
        request.interests
    )

    return gemini_service.generate_json(prompt)