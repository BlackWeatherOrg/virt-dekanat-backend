from typing import Annotated
from fastapi import Depends
from modules.Attendances.repository import AttendanceRepo
from modules.Attendances.service import AttendanceService

AttendanceRepositoryDependency = Annotated[AttendanceRepo, Depends(AttendanceRepo)]


def attendance_service_dependency(repo: AttendanceRepositoryDependency):
    return AttendanceService(attendance_repo=repo)


AttendanceServiceDependency = Annotated[AttendanceService, Depends(attendance_service_dependency)]
