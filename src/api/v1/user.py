from fastapi import APIRouter

from dependencies.auth import AuthServiceDependency
from dependencies.user import UserServiceDependency
from schemas.auth import LoginSchema
from schemas.response.auth import LoginResponse
from schemas.response.user import GetUserResponse
from schemas.user import CreateUserSchema

USER_ROUTER = APIRouter(
    prefix='/auth',
    tags=['auth']
)


# register
@USER_ROUTER.post('/register')
async def register_user(
        service: UserServiceDependency,
        request_data: CreateUserSchema
) -> GetUserResponse:
    user = await service.create(request_data)

    return GetUserResponse(
        message='Success',
        data=user
    )


@USER_ROUTER.post('/login')
async def login_router(
        request_data: LoginSchema,
        service: AuthServiceDependency
) -> LoginResponse:
    data = await service.login(**request_data.model_dump())

    return LoginResponse(
        message='Success',
        access_token=data
    )