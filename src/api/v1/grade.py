from typing import Annotated

from fastapi import APIRouter, Depends

from dependencies.grade import GradeServiceDependency
from modules.Grades.schemas import GetGradeResponse, CreateGradeSchema, SearchGradeSchema, GetManyGradesResponse, \
    UpdateGradeSchema, DefaultGradeResponse, DeleteGradeSchema

GRADE_ROUTER = APIRouter(
    prefix='/grade',
    tags=['grade']
)

@GRADE_ROUTER.post('/create', response_model=GetGradeResponse)
async def create_grade(
        request_data: CreateGradeSchema,
        service: GradeServiceDependency
) -> GetGradeResponse:
    prof = await service.create(request_data)
    return GetGradeResponse(
        message='Grade created',
        data=prof
    )


@GRADE_ROUTER.get('/getOne', response_model=GetGradeResponse)
async def get_grade(
        request_data: Annotated[SearchGradeSchema, Depends(SearchGradeSchema)],
        service: GradeServiceDependency
) -> GetGradeResponse:
    prof = await service.get_one(request_data)
    return GetGradeResponse(
        message='Success',
        data=prof
    )


@GRADE_ROUTER.get('/getMany', response_model=GetManyGradesResponse)
async def list_grades(
        request_data: Annotated[SearchGradeSchema, Depends(SearchGradeSchema)],
        service: GradeServiceDependency
) -> GetManyGradesResponse:
    profs = await service.get_many(request_data)
    return GetManyGradesResponse(
        message='Success',
        data=profs
    )


@GRADE_ROUTER.patch('/update', response_model=GetGradeResponse)
async def update_grade(
        request_data: UpdateGradeSchema,
        service: GradeServiceDependency
) -> GetGradeResponse:
    updated = await service.update_by_id(request_data.id, request_data)
    return GetGradeResponse(
        message='Grade updated',
        data=updated
    )


@GRADE_ROUTER.delete('/delete', response_model=DefaultGradeResponse)
async def delete_grade(
        request_data: Annotated[DeleteGradeSchema, Depends(DeleteGradeSchema)],
        service: GradeServiceDependency
) -> DefaultGradeResponse:
    await service.delete_one(request_data)
    return DefaultGradeResponse(
        message='Grade deleted'
    )

