from fastapi import APIRouter

from car_price_prediction_fastapi.api.routes import prediction

api_router = APIRouter()
api_router.include_router(prediction.router, tags=["prediction"], prefix="/model")
