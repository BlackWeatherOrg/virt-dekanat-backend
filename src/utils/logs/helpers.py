import logging
from time import time
from typing import NotRequired, TypedDict, Unpack

from fastapi.requests import Request

from utils.logs.adapters import ErrorAdapter, RequestsAdapter

ERROR_LOGGER = logging.getLogger('error')
REQUESTS_LOGGER = logging.getLogger('requests')

def calculate_duration(start_time: float) -> int:
    """
    Возвращает округлённое значение времени
    исполнения запроса в мсек
    """
    return round(time()*1000 - start_time)


class RequestsLogData(TypedDict):
    route: str
    body: dict
    query: NotRequired[dict]
    log_type: NotRequired[str]


def exc_to_log(request: Request, **kwargs):
    error_adapter = ErrorAdapter(ERROR_LOGGER, extra=kwargs)
    error_adapter.error('', exc_info=True)


def log_requests(**kwargs: Unpack[RequestsLogData]):
    log_type = kwargs.pop('log_type')
    adapter = RequestsAdapter(REQUESTS_LOGGER, extra=kwargs, log_type=log_type)
    adapter.info('')


def mask_data(data: dict) -> dict:
    mask = {}
    for item, value in data.items():
        mask[item] = value
    return mask


def apply_mask(value: str, rule: dict):
    """Применение маски к значению
    Args:
        value: Значение параметра для маскирования
        rule: Правило для маскирования
    Returns:
        маскированная строка
    """
    if not isinstance(rule, dict):
        return '*' * 15
    start = rule.get('start')
    end = rule.get('end')
    try:
        if isinstance(start, int) and isinstance(end, int):
            return value[:start] + '*' * max(0, len(value) - start - end) + value[-end:]
        elif isinstance(start, str) and '%' in start:
            start = int(len(value) * int(start.replace('%', '')) / 100)
            return '*' * max(0, len(value) - start) + value[start:]
        elif isinstance(end, str) and '%' in end:
            end = int(len(value) * int(end.replace('%', '')) / 100)
            return value[:-end] + '*' * max(0, len(value) - end)
    except (IndexError, TypeError):
        return '*' * len(value)
