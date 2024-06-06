from fastapi import APIRouter, Depends
from starlette.requests import Request

from car_price_prediction_fastapi.core import security
from car_price_prediction_fastapi.models.payload import CarPricePredictionPayload
from car_price_prediction_fastapi.models.prediction import CarPricePredictionResult
from car_price_prediction_fastapi.services.models import CarPriceModel

router = APIRouter()


@router.post("/predict", response_model=CarPricePredictionResult, name="predict")
def post_predict(
    request: Request,
    block_data: CarPricePredictionPayload,
    _: bool = Depends(security.validate_request),
) -> CarPricePredictionResult:
    model: CarPriceModel = request.app.state.model
    prediction: CarPricePredictionResult = model.predict(block_data)

    return prediction
