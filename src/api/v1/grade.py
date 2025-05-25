from typing import Annotated

from fastapi import APIRouter, Depends

from dependencies.discipline import DisciplineServiceDependency
from dependencies.grade import GradeServiceDependency
from dependencies.professor import ProfessorServiceDependency
from dependencies.user import VerifyTokenDependency
from modules.Disciplines.schemas import SearchDisciplineSchema
from modules.Grades.schemas import GetGradeResponse, CreateGradeSchema, SearchGradeSchema, GetManyGradesResponse, \
    UpdateGradeSchema, DefaultGradeResponse, DeleteGradeSchema
from modules.Professors.schemas import SearchProfessorSchema
from utils.base_schema import DefaultResponse

GRADE_ROUTER = APIRouter(
    prefix='/grade',
    tags=['grade']
)

@GRADE_ROUTER.post('/create')
async def create_grade(
        request_data: CreateGradeSchema,
        service: GradeServiceDependency,
        prof_service: ProfessorServiceDependency,
        username: VerifyTokenDependency
) -> GetGradeResponse | DefaultResponse:
    try:
        professor = await prof_service.get_one(SearchProfessorSchema(username=username))
        print(professor.disciplines)
        if request_data.discipline_id not in [item.id for item in professor.disciplines]:
            return DefaultResponse(
                message='You are not a professor of this discipline'
            )

        request_data.professor_id = professor.id
        prof = await service.create(request_data)
        return GetGradeResponse(
            message='Grade created',
            data=prof
        )
    except Exception:
        return DefaultResponse(
            message='Something went wrong'
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

