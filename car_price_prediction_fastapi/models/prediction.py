from pydantic import BaseModel


class CarPricePredictionResult(BaseModel):
    selling_price: float
    currency: str = "INR"
