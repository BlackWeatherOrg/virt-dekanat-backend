from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from api.router import MAIN_ROUTER
from utils.exception_handlers import (incorrect_password_exception_handler,
                                      integrity_exception_handler,
                                      invalid_token_exception_handler,
                                      multiple_results_found_exception_handler,
                                      programming_exception_handler,
                                      unknown_exception_handler,
                                      user_does_not_exist_exception_handler,
                                      validation_exception_handler)
from utils.exceptions import (IncorrectPasswordException, IntegrityException,
                              InvalidTokenException,
                              MultipleResultsFoundException,
                              ObjectDoesNotExistException,
                              ProgrammingException)


def add_exceptions(app):
    app.add_exception_handler(Exception, unknown_exception_handler)
    app.add_exception_handler(RequestValidationError,
                              validation_exception_handler)
    app.add_exception_handler(
        ObjectDoesNotExistException, user_does_not_exist_exception_handler)
    app.add_exception_handler(IntegrityException, integrity_exception_handler)
    app.add_exception_handler(ProgrammingException,
                              programming_exception_handler)
    app.add_exception_handler(
        MultipleResultsFoundException, multiple_results_found_exception_handler)
    app.add_exception_handler(InvalidTokenException,
                              invalid_token_exception_handler)
    app.add_exception_handler(
        IncorrectPasswordException, incorrect_password_exception_handler)


def add_middlewares(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins='*',
        allow_methods='*',
        allow_headers='*',
        allow_credentials=True,
    )


def create_app() -> FastAPI:
    app = FastAPI(
        root_path='/api',
        docs_url='/api/docs'
    )

    app.include_router(MAIN_ROUTER)
    add_exceptions(app)
    add_middlewares(app)

    return app