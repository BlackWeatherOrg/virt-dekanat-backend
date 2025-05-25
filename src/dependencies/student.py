from typing import Annotated
from fastapi import Depends
from modules.Student.repository import StudentRepo
from modules.Student.service import StudentService

StudentRepositoryDependency = Annotated[StudentRepo, Depends(StudentRepo)]


def student_service_dependency(repo: StudentRepositoryDependency):
    return StudentService(student_repo=repo)


StudentServiceDependency = Annotated[StudentService, Depends(student_service_dependency)]
