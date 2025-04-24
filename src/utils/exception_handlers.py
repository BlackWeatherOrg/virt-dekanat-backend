from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse, Response
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from utils.exceptions import (CustomValidationException,
                              IncorrectPasswordException, IntegrityException,
                              InvalidTokenException,
                              MultipleResultsFoundException,
                              ObjectDoesNotExistException,
                              ProgrammingException, UnknownException)


def unknown_exception_handler(request, exc) -> Response:
    _exc = UnknownException()

    return JSONResponse(
        status_code=_exc.status_code,
        content={
            'message': _exc.msg,
            'error_code': _exc.error_code
        },
    )


def validation_exception_handler(request, exc) -> Response:
    validation_exception = CustomValidationException()

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

    return JSONResponse(
        status_code=exc.status_code,
        content={
            'message': exc.msg,
            'error_code': exc.error_code
        },
    )


def integrity_exception_handler(request, exc) -> Response:
    exc = IntegrityException()

    return JSONResponse(
        status_code=exc.status_code,
        content={
            'message': exc.msg,
            'error_code': exc.error_code
        },
    )


def programming_exception_handler(request, exc) -> Response:
    exc = ProgrammingException()

    return JSONResponse(
        status_code=exc.status_code,
        content={
            'message': exc.msg,
            'error_code': exc.error_code
        },
    )


def multiple_results_found_exception_handler(request, exc) -> Response:
    exc = MultipleResultsFoundException()

    return JSONResponse(
        status_code=exc.status_code,
        content={
            'message': exc.msg,
            'error_code': exc.error_code
        },
    )


def invalid_token_exception_handler(request, exc) -> Response:
    exc = InvalidTokenException()

    return JSONResponse(
        status_code=exc.status_code,
        content={
            'message': exc.msg,
            'error_code': exc.error_code
        },
    )


def incorrect_password_exception_handler(request, exc) -> Response:
    exc = IncorrectPasswordException()

    return JSONResponse(
        status_code=exc.status_code,
        content={
            'message': exc.msg,
            'error_code': exc.error_code
        },
    )
