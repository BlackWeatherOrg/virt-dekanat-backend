from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from prometheus_client import make_asgi_app

from settings import settings
from settings.log_config import INFO_LOGGER
from utils.middlewares.logger import LoggerMiddleware

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

    app.add_middleware(LoggerMiddleware)


def create_app() -> FastAPI:
    app = FastAPI(
        root_path='/api'
    )

    app.include_router(MAIN_ROUTER)
    add_exceptions(app)
    add_middlewares(app)

    templates = Jinja2Templates(directory="templates")

    @app.get('/admin', response_class=HTMLResponse)
    def get_admin_page(request: Request):
        return templates.TemplateResponse("admin.html", {"request": request})

    @app.get('/admin/login', response_class=HTMLResponse)
    def get_admin_login(request: Request):
        return templates.TemplateResponse("admin_login.html", {"request": request})

    metrics_app = make_asgi_app()
    app.mount("/metrics", metrics_app)

    INFO_LOGGER.info(f'API STARTED AT http://{settings.HOST}:{settings.PORT}')
    INFO_LOGGER.info(f'API DOCS: http://{settings.HOST}:{settings.PORT}/docs')

    return app
