from typing import Annotated

from fastapi import Depends

from modules.Users.repository import UserRepo
from fastapi.security import OAuth2PasswordBearer
from utils.auth import verify_token
from utils.exceptions import InvalidTokenException
from modules.Users.service import UserService, AuthService

UserRepositoryDependency = Annotated[UserRepo, Depends(UserRepo)]


def user_service_dependency(repo: UserRepositoryDependency):
    return UserService(user_repo=repo)


UserServiceDependency = Annotated[UserService,
                                  Depends(user_service_dependency)]



Oauth2SchemeDependency = Annotated[str, Depends(
    OAuth2PasswordBearer(tokenUrl='token', auto_error=False))]


def verify_token_dep(token: Oauth2SchemeDependency):
    try:
        return verify_token(token)
    except InvalidTokenException:
        raise


VerifyTokenDependency = Annotated[str, Depends(verify_token_dep)]

AuthServiceDependency = Annotated[AuthService, Depends(AuthService)]
