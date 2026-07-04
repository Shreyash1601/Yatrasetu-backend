from fastapi import FastAPI

from api.itinerary import router as itinerary_router
from api.storyteller import router as storyteller_router
from api.hidden_gems import router as hidden_router
from api.food import router as food_router
from api.culture import router as culture_router
from api.events import router as events_router
from api.summary import router as summary_router

app = FastAPI(
    title="YatraSetu AI",
    version="1.0.0"
)

app.include_router(itinerary_router)
app.include_router(storyteller_router)
app.include_router(hidden_router)
app.include_router(food_router)
app.include_router(culture_router)
app.include_router(events_router)
app.include_router(summary_router)


@app.get("/")
def health():
    return {
        "status": "Running",
        "service": "YatraSetu AI Backend"
    }