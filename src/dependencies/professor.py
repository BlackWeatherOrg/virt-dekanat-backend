from typing import Annotated
from fastapi import Depends
from modules.Professors.repository import ProfessorRepo
from modules.Professors.service import ProfessorService

ProfessorRepositoryDependency = Annotated[ProfessorRepo, Depends(ProfessorRepo)]


def professor_service_dependency(repo: ProfessorRepositoryDependency):
    return ProfessorService(professor_repo=repo)


ProfessorServiceDependency = Annotated[ProfessorService, Depends(professor_service_dependency)]
