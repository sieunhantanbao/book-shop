@echo off
call .venv\Scripts\activate
cd app && uvicorn main:app
