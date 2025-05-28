from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse, Response
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from settings.log_config import ERROR_LOGGER

from utils.exceptions import (CustomValidationException,
                              IncorrectPasswordException, IntegrityException,
                              InvalidTokenException,
                              MultipleResultsFoundException,
                              ObjectDoesNotExistException,
                              ProgrammingException, UnknownException)


def unknown_exception_handler(request, exc) -> Response:
    _exc = UnknownException()

    ERROR_LOGGER.error({
        'url': request.url.path,
        'method': request.method,
        'status_code': exc.status_code,
        'error_code': exc.error_code,
        'exc': exc.msg
    })

    return JSONResponse(
        status_code=_exc.status_code,
        content={
            'message': _exc.msg,
            'error_code': _exc.error_code
        },
    )


def validation_exception_handler(request, exc) -> Response:
    validation_exception = CustomValidationException()

    ERROR_LOGGER.error({
        'url': request.url.path,
        'method': request.method,
        'status_code': validation_exception.status_code,
        'error_code': validation_exception.error_code,
        'exc': validation_exception.msg,
        'details': jsonable_encoder(exc.errors())
    })

    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            'message': validation_exception.msg,
            'error_code': validation_exception.error_code,
            'details': jsonable_encoder(exc.errors())
        },
    )


def user_does_not_exist_exception_handler(request, exc) -> Response:
    exc = ObjectDoesNotExistException()

    ERROR_LOGGER.error({
        'url': request.url.path,
        'method': request.method,
        'status_code': exc.status_code,
        'error_code': exc.error_code,
        'exc': exc.msg
    })

    return JSONResponse(
        status_code=exc.status_code,
        content={
            'message': exc.msg,
            'error_code': exc.error_code
        },
    )


def integrity_exception_handler(request, exc) -> Response:
    exc = IntegrityException()

    ERROR_LOGGER.error({
        'url': request.url.path,
        'method': request.method,
        'status_code': exc.status_code,
        'error_code': exc.error_code,
        'exc': exc.msg
    })

    return JSONResponse(
        status_code=exc.status_code,
        content={
            'message': exc.msg,
            'error_code': exc.error_code
        },
    )


def programming_exception_handler(request, exc) -> Response:
    exc = ProgrammingException()

    ERROR_LOGGER.error({
        'url': request.url.path,
        'method': request.method,
        'status_code': exc.status_code,
        'error_code': exc.error_code,
        'exc': exc.msg
    })

    return JSONResponse(
        status_code=exc.status_code,
        content={
            'message': exc.msg,
            'error_code': exc.error_code
        },
    )


def multiple_results_found_exception_handler(request, exc) -> Response:
    exc = MultipleResultsFoundException()

    ERROR_LOGGER.error({
        'url': request.url.path,
        'method': request.method,
        'status_code': exc.status_code,
        'error_code': exc.error_code,
        'exc': exc.msg
    })

    return JSONResponse(
        status_code=exc.status_code,
        content={
            'message': exc.msg,
            'error_code': exc.error_code
        },
    )


def invalid_token_exception_handler(request, exc) -> Response:
    exc = InvalidTokenException()

    ERROR_LOGGER.error({
        'url': request.url.path,
        'method': request.method,
        'status_code': exc.status_code,
        'error_code': exc.error_code,
        'exc': exc.msg
    })

    return JSONResponse(
        status_code=exc.status_code,
        content={
            'message': exc.msg,
            'error_code': exc.error_code
        },
    )


def incorrect_password_exception_handler(request, exc) -> Response:
    exc = IncorrectPasswordException()

    ERROR_LOGGER.error({
        'url': request.url.path,
        'method': request.method,
        'status_code': exc.status_code,
        'error_code': exc.error_code,
        'exc': exc.msg
    })

    return JSONResponse(
        status_code=exc.status_code,
        content={
            'message': exc.msg,
            'error_code': exc.error_code
        },
    )
