from fastapi import APIRouter
from pydantic import BaseModel

from prompts.food_prompt import build_food_prompt
from services.gemini_service import gemini_service

router = APIRouter(prefix="/food", tags=["Food"])


class FoodRequest(BaseModel):
    destination: str


@router.post("/")
def food(request: FoodRequest):

    prompt = build_food_prompt(request.destination)

    return gemini_service.generate_json(prompt)