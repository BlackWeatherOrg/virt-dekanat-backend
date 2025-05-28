from typing import Annotated

from fastapi import APIRouter, Depends

from dependencies.discipline import DisciplineServiceDependency
from dependencies.user import UserServiceDependency, VerifyTokenDependency
from modules.Disciplines.schemas import GetDisciplineResponse, CreateDisciplineSchema, SearchDisciplineSchema, GetManyDisciplinesResponse, \
    UpdateDisciplineSchema, DefaultDisciplineResponse, DeleteDisciplineSchema
from modules.Users.schemas import SearchUserSchema
from utils.base_schema import DefaultResponse

DISCIPLINE_ROUTER = APIRouter(
    prefix='/discipline',
    tags=['discipline']
)

@DISCIPLINE_ROUTER.post('/create', response_model=GetDisciplineResponse)
async def create_discipline(
        request_data: CreateDisciplineSchema,
        service: DisciplineServiceDependency,
        user_service: UserServiceDependency,
        username: VerifyTokenDependency
) -> GetDisciplineResponse | DefaultResponse:
    user = await user_service.get_one(SearchUserSchema(username=username))
    if user.role.id != 2:
        return DefaultResponse(
            message='Only admin can do this.'
        )

    prof = await service.create(request_data)
    return GetDisciplineResponse(
        message='Discipline created',
        data=prof
    )


@DISCIPLINE_ROUTER.get('/getOne', response_model=GetDisciplineResponse)
async def get_discipline(
        request_data: Annotated[SearchDisciplineSchema, Depends(SearchDisciplineSchema)],
        service: DisciplineServiceDependency
) -> GetDisciplineResponse:
    prof = await service.get_one(request_data)
    return GetDisciplineResponse(
        message='Success',
        data=prof
    )


@DISCIPLINE_ROUTER.get('/getMany', response_model=GetManyDisciplinesResponse)
async def list_disciplines(
        request_data: Annotated[SearchDisciplineSchema, Depends(SearchDisciplineSchema)],
        service: DisciplineServiceDependency
) -> GetManyDisciplinesResponse:
    profs = await service.get_many(request_data)
    return GetManyDisciplinesResponse(
        message='Success',
        data=profs
    )


@DISCIPLINE_ROUTER.patch('/update', response_model=GetDisciplineResponse)
async def update_discipline(
        request_data: UpdateDisciplineSchema,
        service: DisciplineServiceDependency
) -> GetDisciplineResponse:
    updated = await service.update_by_id(request_data.id, request_data)
    return GetDisciplineResponse(
        message='Discipline updated',
        data=updated
    )


@DISCIPLINE_ROUTER.delete('/delete', response_model=DefaultDisciplineResponse)
async def delete_discipline(
        request_data: Annotated[DeleteDisciplineSchema, Depends(DeleteDisciplineSchema)],
        service: DisciplineServiceDependency
) -> DefaultDisciplineResponse:
    await service.delete_one(request_data)
    return DefaultDisciplineResponse(
        message='Discipline deleted'
    )

