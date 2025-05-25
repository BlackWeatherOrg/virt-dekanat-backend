from typing import Annotated
from fastapi import Depends
from modules.Groups.repository import GroupRepo
from modules.Groups.service import GroupService

GroupRepositoryDependency = Annotated[GroupRepo, Depends(GroupRepo)]


def group_service_dependency(repo: GroupRepositoryDependency):
    return GroupService(group_repo=repo)


GroupServiceDependency = Annotated[GroupService, Depends(group_service_dependency)]
