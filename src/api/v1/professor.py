from fastapi import APIRouter, Depends
from modules.Professors.schemas import (
    CreateProfessorSchema, SearchProfessorSchema,
    UpdateProfessorSchema, DeleteProfessorSchema,
    GetProfessorResponse, GetManyProfessorsResponse, DefaultProfessorResponse
)
from dependencies.professor import professor_service_dependency
from modules.Professors.service import ProfessorService

PROFESSOR_ROUTER = APIRouter(
    prefix='/professors',
    tags=['professors']
)


@PROFESSOR_ROUTER.post('/create', response_model=GetProfessorResponse)
async def create_professor(
        request_data: CreateProfessorSchema,
        service: ProfessorService = Depends(professor_service_dependency)
) -> GetProfessorResponse:
    prof = await service.create(request_data)
    return GetProfessorResponse(
        message='Professor created',
        data=prof
    )


@PROFESSOR_ROUTER.get('/getOne', response_model=GetProfessorResponse)
async def get_professor(
        request_data: SearchProfessorSchema = Depends(SearchProfessorSchema),
        service: ProfessorService = Depends(professor_service_dependency)
) -> GetProfessorResponse:
    prof = await service.get_one(request_data)
    return GetProfessorResponse(
        message='Success',
        data=prof
    )


@PROFESSOR_ROUTER.get('/getMany', response_model=GetManyProfessorsResponse)
async def list_professors(
        request_data: SearchProfessorSchema = Depends(SearchProfessorSchema),
        service: ProfessorService = Depends(professor_service_dependency)
) -> GetManyProfessorsResponse:
    profs = await service.get_many(request_data)
    return GetManyProfessorsResponse(
        message='Success',
        data=profs
    )


@PROFESSOR_ROUTER.patch('/update', response_model=GetProfessorResponse)
async def update_professor(
        request_data: UpdateProfessorSchema,
        service: ProfessorService = Depends(professor_service_dependency)
) -> GetProfessorResponse:
    updated = await service.update_by_id(request_data.id, request_data)
    return GetProfessorResponse(
        message='Professor updated',
        data=updated
    )


@PROFESSOR_ROUTER.delete('/delete', response_model=DefaultProfessorResponse)
async def delete_professor(
        request_data: DeleteProfessorSchema,
        service: ProfessorService = Depends(professor_service_dependency)
) -> DefaultProfessorResponse:
    await service.delete_one(request_data)
    return DefaultProfessorResponse(
        message='Professor deleted'
    )
