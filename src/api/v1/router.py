from fastapi import APIRouter

from api.v1.user import USER_ROUTER

V1_ROUTER = APIRouter(
    prefix='/v1',
)

V1_ROUTER.include_router(USER_ROUTER)
