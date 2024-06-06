from car_price_prediction_fastapi.core import config
from car_price_prediction_fastapi.models.payload import \
    CarPricePredictionPayload
from car_price_prediction_fastapi.models.prediction import \
    CarPricePredictionResult
from car_price_prediction_fastapi.services.models import CarPriceModel


def test_prediction(test_client) -> None:
    model_path = config.DEFAULT_MODEL_PATH
    cpp = CarPricePredictionPayload.model_validate(
        {
            "present_price": 5.59,
            "kms_driven": 27000,
            "owner": 0,
            "no_year": 4,
            "fuel_type_diesel": 0,
            "fuel_type_petrol": 1,
            "seller_type_individual": 1,
            "transmission_manual": 1,
        }
    )

    cpm = CarPriceModel(model_path)
    result = cpm.predict(cpp)
    assert isinstance(result, CarPricePredictionResult)
