"""
This module is the entry point for the Instagram API.

It creates a FastAPI application and includes the Instagram router.
"""
from fastapi import FastAPI

from routers import instagram


app = FastAPI(title='Instagram API',
              description='A simple API to fetch Instagram photos',
              version='1.0.0')

app.include_router(instagram.router, prefix="/instagram", tags=["Instagram"])
