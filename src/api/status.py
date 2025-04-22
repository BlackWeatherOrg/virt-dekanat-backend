from fastapi import APIRouter

from schemas.base import DefaultResponse

STATUS_ROUTER = APIRouter()


@STATUS_ROUTER.get('/status')
def status() -> DefaultResponse:
    return DefaultResponse(
        message='ok'
    )
