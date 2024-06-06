from typing import Callable

from fastapi import FastAPI
from loguru import logger

from car_price_prediction_fastapi.core.config import DEFAULT_MODEL_PATH
from car_price_prediction_fastapi.services.models import CarPriceModel


def _startup_model(app: FastAPI) -> None:
    model_path = DEFAULT_MODEL_PATH
    print(model_path)
    model_instance = CarPriceModel(model_path)
    app.state.model = model_instance


def _shutdown_model(app: FastAPI) -> None:
    app.state.model = None


def start_app_handler(app: FastAPI) -> Callable:
    def startup() -> None:
        logger.info("Running app start handler.")
        _startup_model(app)

    return startup


def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        logger.info("Running app shutdown handler.")
        _shutdown_model(app)

    return shutdown
