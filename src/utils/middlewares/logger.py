import time
import typing

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response, StreamingResponse

from settings.log_config import REQUESTS_LOGGER
from utils.logs.helpers import log_requests, calculate_duration


class LoggerMiddleware(BaseHTTPMiddleware):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        # Добавление времени начала запроса в его контекст
        request.state.start_time = time.time() * 1000
        # Чтение и сохранение тела запроса
        # req_body = await request.body() (нет ручек кроме GET)

        # Обработка запроса и получение ответа
        response = typing.cast(StreamingResponse, await call_next(request))

        # Чтение тела ответа
        res_body: bytes = b''
        async for chunk in response.body_iterator:
            res_body += chunk if isinstance(chunk, bytes) else chunk.encode()

        # Логирование ответа
        duration = calculate_duration(request.state.start_time)
        log_requests(
            method=request.method,
            status=response.status_code,
            route=request.url.path,
            resp_size=len(res_body),
            log_type='response',
            duration=duration)

        # Формирование и возвращение ответа
        return Response(content=res_body, status_code=response.status_code, headers=dict(response.headers), media_type=response.media_type)
