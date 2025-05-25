from typing import Annotated
from fastapi import Depends
from modules.Grades.repository import GradeRepo
from modules.Grades.service import GradeService

GradeRepositoryDependency = Annotated[GradeRepo, Depends(GradeRepo)]


def grade_service_dependency(repo: GradeRepositoryDependency):
    return GradeService(grade_repo=repo)


GradeServiceDependency = Annotated[GradeService, Depends(grade_service_dependency)]
