from typing import Annotated

from fastapi import APIRouter, Depends

from dependencies.user import UserServiceDependency, AuthServiceDependency, VerifyTokenDependency
from utils.base_schema import DefaultResponse
from modules.Users.schemas import LoginSchema, SearchUserSchema, GetManyUsersResponse, UpdateUserSchema, ChangePasswordSchema, \
    DeleteUserSchema
from modules.Users.schemas import LoginResponse
from modules.Users.schemas import GetUserResponse
from modules.Users.schemas import CreateUserSchema

AUTH_ROUTER = APIRouter(
    prefix='/auth',
    tags=['auth']
)


# register
@AUTH_ROUTER.post('/register')
async def register_user(
        service: UserServiceDependency,
        request_data: CreateUserSchema
) -> GetUserResponse:
    user = await service.create(request_data)

    return GetUserResponse(
        message='Success',
        data=user
    )


@AUTH_ROUTER.post('/login')
async def login_router(
        request_data: LoginSchema,
        service: AuthServiceDependency
) -> LoginResponse:
    data = await service.login(**request_data.model_dump())

    return LoginResponse(
        message='Success',
        access_token=data
    )

USER_ROUTER = APIRouter(
    prefix='/user',
    tags=['user']
)

# get


@USER_ROUTER.get('/getOne')
async def get_one(
        request_data: Annotated[SearchUserSchema, Depends(SearchUserSchema)],
        service: UserServiceDependency
) -> GetUserResponse:
    users = await service.get_one(request_data)

    return GetUserResponse(
        message='Success',
        data=users
    )


@USER_ROUTER.get('/getMany')
async def get_many(
        request_data: Annotated[SearchUserSchema, Depends(SearchUserSchema)],
        service: UserServiceDependency
) -> GetManyUsersResponse:
    users = await service.get_many(request_data)

    return GetManyUsersResponse(
        message='Success',
        data=users
    )


# update
@USER_ROUTER.patch('/update')
async def update_self(
        request_data: UpdateUserSchema,
        service: UserServiceDependency,
        email: VerifyTokenDependency
) -> GetUserResponse:
    user = await service.get_one(SearchUserSchema(email=email))

    upd_user = await service.update_by_id(user.id, request_data)

    return GetUserResponse(
        message='Success',
        data=upd_user
    )


@USER_ROUTER.patch('/changePassword')
async def change_password(
        request_data: ChangePasswordSchema,
        service: UserServiceDependency,
        email: VerifyTokenDependency
) -> DefaultResponse:
    await service.change_password(email, request_data.old_password, request_data.new_password)

    return DefaultResponse(
        message='Password changed successfully'
    )


# delete
@USER_ROUTER.delete('/delete')
async def delete(
        service: UserServiceDependency,
        email: VerifyTokenDependency
) -> DefaultResponse:
    user = await service.get_one(SearchUserSchema(email=email))

    await service.delete_one(DeleteUserSchema(id=user.id))
    return DefaultResponse(
        message='Success',
    )


@USER_ROUTER.get('/current')
async def current(
        service: UserServiceDependency,
        email: VerifyTokenDependency
) -> GetUserResponse:
    user = await service.get_one(SearchUserSchema(email=email))

    return GetUserResponse(
        message='Success',
        data=user
    )
