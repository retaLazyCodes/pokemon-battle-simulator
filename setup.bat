@echo off

python -m venv venv

call venv\Scripts\activate

pip install poetry

poetry install --no-dev

python src\main.py
