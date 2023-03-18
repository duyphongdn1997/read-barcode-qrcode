"""API Routes."""
from fastapi import APIRouter

from app.api.routes import barcode_api

routes = APIRouter()

routes.include_router(barcode_api.router, prefix="/v1")
