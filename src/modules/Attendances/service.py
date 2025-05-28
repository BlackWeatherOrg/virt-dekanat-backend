from modules.Attendances.repository import AttendanceRepo
from modules.Attendances.schemas import (
    CreateAttendanceSchema, SearchAttendanceSchema,
    UpdateAttendanceSchema, DeleteAttendanceSchema, GetAttendanceSchema
)


class AttendanceService:
    def __init__(self, attendance_repo: AttendanceRepo):
        self._repo = attendance_repo

    async def create(self, data: CreateAttendanceSchema) -> GetAttendanceSchema:
        attendance = await self._repo.create_one(data.model_dump(exclude_none=True))
        return attendance

    async def get_one(self, data: SearchAttendanceSchema) -> GetAttendanceSchema:
        attendance = await self._repo.get_one(data.model_dump(exclude_none=True))
        return attendance

    async def get_many(self, data: SearchAttendanceSchema) -> list[GetAttendanceSchema]:
        attendances = await self._repo.get_many(data.model_dump(exclude_none=True))
        return attendances

    async def update_by_id(self, attendance_id: int, data: UpdateAttendanceSchema) -> GetAttendanceSchema:
        attendance = await self._repo.update_by_id(attendance_id, data.model_dump(exclude_none=True))
        return attendance

    async def delete_one(self, data: DeleteAttendanceSchema) -> None:
        await self._repo.delete_one(data.model_dump(exclude_none=True))

    async def delete_many(self, data: DeleteAttendanceSchema) -> None:
        await self._repo.delete_many(data.model_dump(exclude_none=True))
