from typing import Annotated

from fastapi import APIRouter, Depends

from dependencies.discipline import DisciplineServiceDependency
from dependencies.dopusk import DopuskServiceDependency
from dependencies.professor import ProfessorServiceDependency
from dependencies.student import StudentServiceDependency
from dependencies.user import VerifyTokenDependency
from modules.Disciplines.schemas import SearchDisciplineSchema
from modules.Dopusk.schemas import GetDopuskResponse, CreateDopuskSchema, SearchDopuskSchema, GetManyDopusksResponse, \
    UpdateDopuskSchema, DefaultDopuskResponse, DeleteDopuskSchema
from modules.Professors.schemas import SearchProfessorSchema
from modules.Student.schemas import SearchStudentSchema
from utils.base_schema import DefaultResponse

DOPUSK_ROUTER = APIRouter(
    prefix='/dopusk',
    tags=['dopusk']
)

@DOPUSK_ROUTER.post('/create')
async def create_dopusk(
        request_data: CreateDopuskSchema,
        service: DopuskServiceDependency,
        stud_service: StudentServiceDependency,
        username: VerifyTokenDependency
) -> GetDopuskResponse | DefaultResponse:
    try:
        student = await stud_service.get_one(SearchStudentSchema(username=username))

        request_data.student_id = student.id
        dopusk = await service.create(request_data)
        return GetDopuskResponse(
            message='Dopusk created',
            data=dopusk
        )
    except Exception:
        return DefaultResponse(
            message='Something went wrong'
        )
