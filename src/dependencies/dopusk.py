from typing import Annotated
from fastapi import Depends
from modules.Dopusk.repository import DopuskRepo
from modules.Dopusk.service import DopuskService

DopuskRepositoryDependency = Annotated[DopuskRepo, Depends(DopuskRepo)]


def dopusk_service_dependency(repo: DopuskRepositoryDependency):
    return DopuskService(dopusk_repo=repo)


DopuskServiceDependency = Annotated[DopuskService, Depends(dopusk_service_dependency)]
