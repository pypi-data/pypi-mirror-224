from fastapi import FastAPI

from myevery import create_service

app: FastAPI = create_service(
    "examples.ex1:chain",
)
