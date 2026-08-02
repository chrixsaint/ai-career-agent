from fastapi import FastAPI

from .api.routers import system

app = FastAPI()

app.include_router(system.router)