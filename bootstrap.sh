#!/bin/bash
export BACKEND_CONFIG=./backend/keys_config.cfg
export FLASK_APP=./backend/index.py
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0