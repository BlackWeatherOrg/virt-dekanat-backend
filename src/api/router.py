from fastapi import APIRouter

from api.status import STATUS_ROUTER
from api.v1.router import V1_ROUTER

MAIN_ROUTER = APIRouter()

MAIN_ROUTER.include_router(STATUS_ROUTER)
MAIN_ROUTER.include_router(V1_ROUTER)