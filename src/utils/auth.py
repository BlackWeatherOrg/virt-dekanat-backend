from datetime import datetime, timedelta

from jose import JWTError, jwt

from settings import settings
from utils.exceptions import InvalidTokenException


def encode_access_token(username: str) -> str:
    expire = datetime.now() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {'username': username, 'exp': expire}

    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str) -> dict:
    payload = jwt.decode(token, settings.SECRET_KEY,
                         algorithms=[settings.ALGORITHM])
    return payload


def verify_token(token: str) -> str:
    """Функция для проверки валидности токена.
    При включенном режиме DEBUG пропускает проверку авторизации

    Args:
        token: авторизационный токен доступа

    Returns:
        Имя пользователя
    """
    if not token:
        raise InvalidTokenException()

    try:
        payload = jwt.decode(token, settings.SECRET_KEY,
                             algorithms=[settings.ALGORITHM])

        username = payload.get('username')
        if not username:
            raise InvalidTokenException()

        return username

    except JWTError:
        raise InvalidTokenException()
