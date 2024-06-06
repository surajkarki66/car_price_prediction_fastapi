from car_price_prediction_fastapi.core import config


def test_prediction(test_client) -> None:
    response = test_client.post(
        "/api/v1/model/predict",
        json={
            "present_price": 3.3,
            "kms_driven": 2330,
            "owner": 1,
            "no_year": 10,
            "fuel_type_diesel": 1,
            "fuel_type_petrol": 0,
            "seller_type_individual": 1,
            "transmission_manual": 0
            },
        headers={"token": str(config.API_KEY)},
        )
    assert response.status_code == 200
    assert "selling_price" in response.json()
    assert "currency" in response.json()


def test_prediction_nopayload(test_client) -> None:
    response = test_client.post(
        "/api/v1/model/predict", json={}, headers={"token": str(config.API_KEY)}
        )
    assert response.status_code == 422
