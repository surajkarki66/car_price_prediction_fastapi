#!/usr/bin/env bash

set -xe

pytest -vv --cov=car_price_prediction_fastapi --cov=tests --cov-report=term-missing --cov-report=xml tests/ ${@}
