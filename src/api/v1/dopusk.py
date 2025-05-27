from typing import Annotated

from fastapi import APIRouter, Depends

from dependencies.discipline import DisciplineServiceDependency
from dependencies.dopusk import DopuskServiceDependency
from dependencies.professor import ProfessorServiceDependency
from dependencies.user import VerifyTokenDependency
from modules.Disciplines.schemas import SearchDisciplineSchema
from modules.Dopusk.schemas import GetDopuskResponse, CreateDopuskSchema, SearchDopuskSchema, GetManyDopusksResponse, \
    UpdateDopuskSchema, DefaultDopuskResponse, DeleteDopuskSchema
from modules.Professors.schemas import SearchProfessorSchema
from utils.base_schema import DefaultResponse

DOPUSK_ROUTER = APIRouter(
    prefix='/dopusk',
    tags=['dopusk']
)

@DOPUSK_ROUTER.post('/create')
async def create_dopusk(
        request_data: CreateDopuskSchema,
        service: DopuskServiceDependency,
        prof_service: ProfessorServiceDependency,
        username: VerifyTokenDependency
) -> GetDopuskResponse | DefaultResponse:
    try:
        professor = await prof_service.get_one(SearchProfessorSchema(username=username))
        print(professor.disciplines)
        if request_data.discipline_id not in [item.id for item in professor.disciplines]:
            return DefaultResponse(
                message='You are not a professor of this discipline'
            )

        request_data.professor_id = professor.id
        prof = await service.create(request_data)
        return GetDopuskResponse(
            message='Dopusk created',
            data=prof
        )
    except Exception:
        return DefaultResponse(
            message='Something went wrong'
        )
