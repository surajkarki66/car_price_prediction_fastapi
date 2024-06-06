#! /usr/bin/env bash

set -xe

isort .

mypy --install-types --non-interactive car_price_prediction_fastapi/

mypy car_price_prediction_fastapi

black car_price_prediction_fastapi --line-length 88

flake8 car_price_prediction_fastapi

bandit -r car_price_prediction_fastapi/
