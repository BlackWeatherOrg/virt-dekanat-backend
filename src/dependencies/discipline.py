from typing import Annotated
from fastapi import Depends
from modules.Disciplines.repository import DisciplineRepo
from modules.Disciplines.service import DisciplineService

DisciplineRepositoryDependency = Annotated[DisciplineRepo, Depends(DisciplineRepo)]


def discipline_service_dependency(repo: DisciplineRepositoryDependency):
    return DisciplineService(discipline_repo=repo)


DisciplineServiceDependency = Annotated[DisciplineService, Depends(discipline_service_dependency)]
