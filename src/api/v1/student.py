from typing import Annotated

from fastapi import APIRouter, Depends

from dependencies.user import AuthServiceDependency, VerifyTokenDependency
from modules.Student.schemas import (
    CreateStudentSchema, SearchStudentSchema,
    UpdateStudentSchema, DeleteStudentSchema,
    GetStudentResponse, GetManyStudentsResponse, DefaultStudentResponse
)
from dependencies.student import StudentServiceDependency
from modules.Users.schemas import ChangePasswordSchema
from utils.base_schema import DefaultResponse

STUDENT_ROUTER = APIRouter(
    prefix='/student',
    tags=['student']
)


@STUDENT_ROUTER.post('/create', response_model=GetStudentResponse)
async def create_student(
        request_data: CreateStudentSchema,
        service: StudentServiceDependency
) -> GetStudentResponse:
    prof = await service.create(request_data)
    return GetStudentResponse(
        message='Student created',
        data=prof
    )


@STUDENT_ROUTER.get('/getOne', response_model=GetStudentResponse)
async def get_student(
        request_data: Annotated[SearchStudentSchema, Depends(SearchStudentSchema)],
        service: StudentServiceDependency
) -> GetStudentResponse:
    prof = await service.get_one(request_data)
    return GetStudentResponse(
        message='Success',
        data=prof
    )


@STUDENT_ROUTER.get('/getMany', response_model=GetManyStudentsResponse)
async def list_students(
        request_data: Annotated[SearchStudentSchema, Depends(SearchStudentSchema)],
        service: StudentServiceDependency
) -> GetManyStudentsResponse:
    profs = await service.get_many(request_data)
    return GetManyStudentsResponse(
        message='Success',
        data=profs
    )
