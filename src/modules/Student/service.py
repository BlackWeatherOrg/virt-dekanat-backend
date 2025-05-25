from modules.Student.repository import StudentRepo
from modules.Student.schemas import (CreateStudentSchema, DeleteStudentSchema, GetStudentSchema,
                                   SearchStudentSchema, UpdateStudentSchema)


class StudentService:
    def __init__(self, student_repo: StudentRepo):
        self._student_repo: StudentRepo = student_repo

    async def create(
            self,
            data: CreateStudentSchema
    ) -> GetStudentSchema:
        """
        Создать пользователя по параметрам

        Returns:
            Созданный пользователь
        """
        student = await self._student_repo.create_one(data.model_dump(exclude_none=True))

        return student

    async def get_one(self, data: SearchStudentSchema) -> GetStudentSchema:
        """
        Возвращает информацтю о пользователе по id

        Returns:
            Информация о польозвателе
        """
        student = await self._student_repo.get_one(data.model_dump(exclude_none=True))

        return student

    async def get_many(self, data: SearchStudentSchema) -> list[GetStudentSchema]:
        students = await self._student_repo.get_many(data.model_dump(exclude_none=True))

        return students

    async def update_by_id(
            self,
            student_id: int,
            data: UpdateStudentSchema
    ) -> GetStudentSchema:
        """
        Обновить информацию о пользователе по id

        Returns:
            Информация об обновленном пользователе
        """
        student = await self._student_repo.update_by_id(
            student_id,
            data.model_dump(exclude_none=True)
        )

        return student

    async def delete_one(self, data: DeleteStudentSchema) -> None:
        """
        Удалить пользователя по id
        """

        await self._student_repo.delete_one(data.model_dump(exclude_none=True))

    async def delete_many(self, data: DeleteStudentSchema) -> None:
        """
        Удалить пользователя по id
        """

        await self._student_repo.delete_many(data.model_dump(exclude_none=True))
