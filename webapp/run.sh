#!/bin/sh

export FLASK_APP=app.py
export PYTHONPATH=/app/sqlparse

python3 -m flask run --host=0.0.0.0
