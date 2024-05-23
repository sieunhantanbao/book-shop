#!/bin/bash
source .venv/bin/activate
cd app && uvicorn main:app
