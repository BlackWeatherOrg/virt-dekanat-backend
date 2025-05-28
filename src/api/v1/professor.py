from typing import Annotated

from fastapi import APIRouter, Depends

from dependencies.user import AuthServiceDependency, VerifyTokenDependency, UserServiceDependency
from modules.Professors.schemas import (
    CreateProfessorSchema, SearchProfessorSchema,
    UpdateProfessorSchema, DeleteProfessorSchema,
    GetProfessorResponse, GetManyProfessorsResponse, DefaultProfessorResponse
)
from dependencies.professor import ProfessorServiceDependency
from modules.Users.schemas import ChangePasswordSchema, SearchUserSchema
from utils.base_schema import DefaultResponse

PROFESSOR_ROUTER = APIRouter(
    prefix='/professor',
    tags=['professor']
)


@PROFESSOR_ROUTER.post('/create')
async def create_professor(
        request_data: CreateProfessorSchema,
        service: ProfessorServiceDependency,
        user_service: UserServiceDependency,
        username: VerifyTokenDependency
) -> GetProfessorResponse | DefaultResponse:
    user = await user_service.get_one(SearchUserSchema(username=username))
    if user.role.id != 2:
        return DefaultResponse(
            message='Only admin can do this.'
        )
    prof = await service.create(request_data)
    return GetProfessorResponse(
        message='Professor created',
        data=prof
    )


@PROFESSOR_ROUTER.get('/getOne', response_model=GetProfessorResponse)
async def get_professor(
        request_data: Annotated[SearchProfessorSchema, Depends(SearchProfessorSchema)],
        service: ProfessorServiceDependency
) -> GetProfessorResponse:
    prof = await service.get_one(request_data)
    return GetProfessorResponse(
        message='Success',
        data=prof
    )


@PROFESSOR_ROUTER.get('/getMany', response_model=GetManyProfessorsResponse)
async def list_professors(
        request_data: Annotated[SearchProfessorSchema, Depends(SearchProfessorSchema)],
        service: ProfessorServiceDependency
) -> GetManyProfessorsResponse:
    profs = await service.get_many(request_data)
    return GetManyProfessorsResponse(
        message='Success',
        data=profs
    )


# @PROFESSOR_ROUTER.patch('/update', response_model=GetProfessorResponse)
# async def update_professor(
#         request_data: UpdateProfessorSchema,
#         service: ProfessorServiceDependency,
#         professor_auth: VerifyTokenDependency
# ) -> GetProfessorResponse | DefaultProfessorResponse:
#     if 'pr' not in professor_auth:
#         return DefaultProfessorResponse(
#             message='You are not professor'
#         )
#
#     updated = await service.update_by_id(request_data.id, request_data)
#     return GetProfessorResponse(
#         message='Professor updated',
#         data=updated
#     )


# @PROFESSOR_ROUTER.delete('/delete', response_model=DefaultProfessorResponse)
# async def delete_professor(
#         request_data: Annotated[DeleteProfessorSchema, Depends(DeleteProfessorSchema)],
#         service: ProfessorServiceDependency,
#         professor_auth: VerifyTokenDependency
# ) -> DefaultProfessorResponse:
#     if 'pr' not in professor_auth:
#         return DefaultProfessorResponse(
#             message='You are not professor'
#         )
#
#     await service.delete_one(request_data)
#     return DefaultProfessorResponse(
#         message='Professor deleted'
#     )
