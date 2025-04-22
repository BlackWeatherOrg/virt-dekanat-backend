from fastapi import HTTPException

from reposotories.user import UserRepo
from utils.auth import encode_access_token
from utils.password_utils import verify_password


class AuthService:
    """Cервис для аутентификации пользователей"""

    def __init__(self):
        self.repository = UserRepo()

    async def login(self, email: str, password: str) -> str:
        """Функция авторизации, генерирует jwt токен

        Args:
            email: почта для входа
            password: пароль для входа

        Returns:
            str: jwt token
        """

        if user_password := await self.repository.get_password(email):
            if verify_password(password, user_password):
                return encode_access_token(email)
        raise HTTPException(status_code=403, detail='Invalid credentials')


from fastapi import HTTPException, UploadFile

from reposotories.user import UserRepo
from schemas.blog import GetBlogSchema
from schemas.user import (CreateUserSchema, DeleteUserSchema, GetUserSchema,
                          SearchUserSchema, UpdateUserSchema)
from settings.log_config import ERROR_LOGGER
from utils.enums import RolesEnum
from utils.exceptions import IncorrectPasswordException
from utils.object_storage import (delete_file_from_obj_storage,
                                  upload_file_to_obj_storage)
from utils.password_utils import get_password_hash, verify_password


class UserService:
    def __init__(self, user_repo: UserRepo):
        self._user_repo: UserRepo = user_repo

    async def create(
            self,
            data: CreateUserSchema
    ) -> GetUserSchema:
        """
        Создать пользователя по параметрам

        Returns:
            Созданный пользователь
        """
        user = await self._user_repo.create_one(data.model_dump(exclude_none=True))

        return user

    async def get_one(self, data: SearchUserSchema) -> GetUserSchema:
        """
        Возвращает информацтю о пользователе по id

        Returns:
            Информация о польозвателе
        """
        user = await self._user_repo.get_one(data.model_dump(exclude_none=True))

        return user

    async def get_many(self, data: SearchUserSchema) -> list[GetUserSchema]:
        users = await self._user_repo.get_many(data.model_dump(exclude_none=True))

        return users

    async def update_by_id(
            self,
            user_id: int,
            data: UpdateUserSchema
    ) -> GetUserSchema:
        """
        Обновить информацию о пользователе по id

        Returns:
            Информация об обновленном пользователе
        """
        user = await self._user_repo.update_by_id(
            user_id,
            data.model_dump(exclude_none=True)
        )

        return user

    async def delete_one(self, data: DeleteUserSchema) -> None:
        """
        Удалить пользователя по id
        """

        await self._user_repo.delete_one(data.model_dump(exclude_none=True))

    async def delete_many(self, data: DeleteUserSchema) -> None:
        """
        Удалить пользователя по id
        """

        await self._user_repo.delete_many(data.model_dump(exclude_none=True))

    async def change_password(self, email, old_password: str, new_password: str):
        if user_password := await self._user_repo.get_password(email):
            if verify_password(old_password, user_password):
                user = await self.get_one(SearchUserSchema(email=email))
                await self._user_repo.update_by_id(user.id, {'password': get_password_hash(new_password)})
            else:
                raise IncorrectPasswordException

    async def grant_role(self, user: GetUserSchema, role: RolesEnum):
        await self._user_repo.update_by_id(user.id, {'role': role})
