from typing import Annotated

from fastapi import APIRouter, Depends

from dependencies.group import GroupServiceDependency
from modules.Groups.schemas import GetGroupResponse, CreateGroupSchema, SearchGroupSchema, GetManyGroupsResponse, \
    UpdateGroupSchema, DefaultGroupResponse, DeleteGroupSchema

GROUP_ROUTER = APIRouter(
    prefix='/group',
    tags=['group']
)

@GROUP_ROUTER.post('/create', response_model=GetGroupResponse)
async def create_group(
        request_data: CreateGroupSchema,
        service: GroupServiceDependency
) -> GetGroupResponse:
    prof = await service.create(request_data)
    return GetGroupResponse(
        message='Group created',
        data=prof
    )


@GROUP_ROUTER.get('/getOne', response_model=GetGroupResponse)
async def get_group(
        request_data: Annotated[SearchGroupSchema, Depends(SearchGroupSchema)],
        service: GroupServiceDependency
) -> GetGroupResponse:
    prof = await service.get_one(request_data)
    return GetGroupResponse(
        message='Success',
        data=prof
    )


@GROUP_ROUTER.get('/getMany', response_model=GetManyGroupsResponse)
async def list_groups(
        request_data: Annotated[SearchGroupSchema, Depends(SearchGroupSchema)],
        service: GroupServiceDependency
) -> GetManyGroupsResponse:
    profs = await service.get_many(request_data)
    return GetManyGroupsResponse(
        message='Success',
        data=profs
    )


@GROUP_ROUTER.patch('/update', response_model=GetGroupResponse)
async def update_group(
        request_data: UpdateGroupSchema,
        service: GroupServiceDependency
) -> GetGroupResponse:
    updated = await service.update_by_id(request_data.id, request_data)
    return GetGroupResponse(
        message='Group updated',
        data=updated
    )


@GROUP_ROUTER.delete('/delete', response_model=DefaultGroupResponse)
async def delete_group(
        request_data: Annotated[DeleteGroupSchema, Depends(DeleteGroupSchema)],
        service: GroupServiceDependency
) -> DefaultGroupResponse:
    await service.delete_one(request_data)
    return DefaultGroupResponse(
        message='Group deleted'
    )

