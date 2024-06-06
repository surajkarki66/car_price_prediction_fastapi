import numpy as np
from loguru import logger
from skops.io import load

from car_price_prediction_fastapi.models.payload import (
    CarPricePredictionPayload,
    payload_to_list,
)
from car_price_prediction_fastapi.models.prediction import CarPricePredictionResult


class CarPriceModel:
    RESULT_UNIT_FACTOR = 100000

    def __init__(self, path: str) -> None:
        self.path = path
        self._load_local_model()

    def _load_local_model(self) -> None:
        self.model = load(self.path, trusted=True)

    def _pre_process(self, payload: CarPricePredictionPayload) -> np.ndarray:
        logger.debug("Pre-processing payload.")
        result = np.asarray(payload_to_list(payload)).reshape(1, -1)
        return result

    def _post_process(self, prediction: np.ndarray) -> CarPricePredictionResult:
        logger.debug("Post-processing prediction.")
        result = prediction.tolist()
        human_readable_unit = result[0] * self.RESULT_UNIT_FACTOR
        cpp = CarPricePredictionResult(selling_price=int(human_readable_unit))
        return cpp

    def _predict(self, features: np.ndarray) -> np.ndarray:
        logger.debug("Predicting.")
        prediction_result = self.model.predict(features)
        return prediction_result

    def predict(self, payload: CarPricePredictionPayload) -> CarPricePredictionResult:
        pre_processed_payload = self._pre_process(payload)
        prediction = self._predict(pre_processed_payload)
        logger.info(prediction)
        post_processed_result = self._post_process(prediction)

        return post_processed_result
