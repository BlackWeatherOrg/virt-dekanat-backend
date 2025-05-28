from typing import Annotated

from fastapi import APIRouter, Depends

from dependencies.attendance import AttendanceServiceDependency
from dependencies.professor import ProfessorServiceDependency
from dependencies.user import VerifyTokenDependency
from modules.Attendances.schemas import GetAttendanceResponse, CreateAttendanceSchema, SearchAttendanceSchema, GetManyAttendancesResponse, \
    UpdateAttendanceSchema, DefaultAttendanceResponse, DeleteAttendanceSchema
from modules.Professors.schemas import SearchProfessorSchema
from utils.base_schema import DefaultResponse

ATTENDANCE_ROUTER = APIRouter(
    prefix='/attendance',
    tags=['attendance']
)

@ATTENDANCE_ROUTER.post('/create')
async def create_attendance(
        request_data: CreateAttendanceSchema,
        service: AttendanceServiceDependency,
        prof_service: ProfessorServiceDependency,
        username: VerifyTokenDependency
) -> GetAttendanceResponse | DefaultResponse:
    try:
        professor = await prof_service.get_one(SearchProfessorSchema(username=username))
        if request_data.discipline_id not in [item.id for item in professor.disciplines]:
            return DefaultResponse(
                message='You are not a professor of this discipline'
            )

        prof = await service.create(request_data)
        return GetAttendanceResponse(
            message='Attendance created',
            data=prof
        )
    except Exception as e:
        raise e
        return DefaultResponse(
            message='Something went wrong'
        )



@ATTENDANCE_ROUTER.get('/getOne', response_model=GetAttendanceResponse)
async def get_attendance(
        request_data: Annotated[SearchAttendanceSchema, Depends(SearchAttendanceSchema)],
        service: AttendanceServiceDependency
) -> GetAttendanceResponse:
    prof = await service.get_one(request_data)
    return GetAttendanceResponse(
        message='Success',
        data=prof
    )


@ATTENDANCE_ROUTER.get('/getMany', response_model=GetManyAttendancesResponse)
async def list_attendances(
        request_data: Annotated[SearchAttendanceSchema, Depends(SearchAttendanceSchema)],
        service: AttendanceServiceDependency
) -> GetManyAttendancesResponse:
    profs = await service.get_many(request_data)
    return GetManyAttendancesResponse(
        message='Success',
        data=profs
    )


@ATTENDANCE_ROUTER.patch('/update', response_model=GetAttendanceResponse)
async def update_attendance(
        request_data: UpdateAttendanceSchema,
        service: AttendanceServiceDependency
) -> GetAttendanceResponse:
    updated = await service.update_by_id(request_data.id, request_data)
    return GetAttendanceResponse(
        message='Attendance updated',
        data=updated
    )


@ATTENDANCE_ROUTER.delete('/delete', response_model=DefaultAttendanceResponse)
async def delete_attendance(
        request_data: Annotated[DeleteAttendanceSchema, Depends(DeleteAttendanceSchema)],
        service: AttendanceServiceDependency
) -> DefaultAttendanceResponse:
    await service.delete_one(request_data)
    return DefaultAttendanceResponse(
        message='Attendance deleted'
    )

