

import pytest
from starlette.config import environ
from starlette.testclient import TestClient

environ["API_KEY"] = "be01b523-7b00-47c2-855d-7d63384c1c01"
environ["DEFAULT_MODEL_PATH"] = "./model/car_price_prediction_rf.skops"

from car_price_prediction_fastapi.main import get_app  # noqa: E402


@pytest.fixture()
def test_client():
    app = get_app()
    with TestClient(app) as test_client:
        yield test_client
