#!/bin/bash
export BACKEND_CONFIG=../backend/keys_config.cfg
source $(pipenv --venv)/bin/activate
python start-db.py