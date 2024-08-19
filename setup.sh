#!/bin/bash

python3 -m venv venv

source venv/bin/activate

pip install poetry

poetry install --no-dev

python src/main.py
