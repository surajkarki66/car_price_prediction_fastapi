from enum import Enum
from typing import List

import numpy as np
from pydantic import BaseModel


class BinaryEnum(int, Enum):
    ZERO = 0
    ONE = 1


class CarPricePredictionPayload(BaseModel):
    present_price: float
    kms_driven: int
    owner: int
    no_year: int
    fuel_type_diesel: BinaryEnum
    fuel_type_petrol: BinaryEnum
    seller_type_individual: BinaryEnum
    transmission_manual: BinaryEnum


def payload_to_list(cpp: CarPricePredictionPayload) -> List:
    return [
        cpp.present_price,
        np.log(cpp.kms_driven),
        cpp.owner,
        cpp.no_year,
        cpp.fuel_type_diesel,
        cpp.fuel_type_petrol,
        cpp.seller_type_individual,
        cpp.transmission_manual,
    ]
