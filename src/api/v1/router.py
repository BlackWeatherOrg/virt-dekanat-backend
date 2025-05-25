from fastapi import APIRouter

from api.v1.discipline import DISCIPLINE_ROUTER
from api.v1.grade import GRADE_ROUTER
from api.v1.user import USER_ROUTER, AUTH_ROUTER
from api.v1.professor import PROFESSOR_ROUTER

V1_ROUTER = APIRouter(
    prefix='/v1',
)

V1_ROUTER.include_router(AUTH_ROUTER)
V1_ROUTER.include_router(USER_ROUTER)
V1_ROUTER.include_router(PROFESSOR_ROUTER)
V1_ROUTER.include_router(GRADE_ROUTER)
V1_ROUTER.include_router(DISCIPLINE_ROUTER)
