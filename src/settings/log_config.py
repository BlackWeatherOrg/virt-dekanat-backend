import sys
from datetime import datetime
import logging

from settings import settings


INFO_LOGGER = logging.getLogger('info')
REQUESTS_LOGGER = logging.getLogger('requests')
ERROR_LOGGER = logging.getLogger('error')


LOGGER_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'json': {'()': 'utils.logs.formatters.JSONFormatter'},
        'console': {'()': 'utils.logs.formatters.ConsoleFormatter'},
    },
    'handlers': {
        'console': {
            'level': settings.LOG_LEVEL,
            'formatter': 'console',
            'class': 'logging.StreamHandler',
        },
        'file_handler': {
            'formatter': 'json',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': f'{settings.LOG_DIR}/logs.json',
            'when': 'midnight',
            'backupCount': 0
        },
        'null': {
            'class': 'logging.NullHandler'
        },
    },
    'loggers': {
        'root': {
            'level': settings.LOG_LEVEL,
            'handlers': ['console'],
            'propagate': False,
        },
        'requests': {
            'handlers': ['file_handler'],
            'level': logging.INFO,
            'propagate': True,
        },
        'error': {
            'handlers': ['file_handler'],
            'level': logging.ERROR,
            'propagate': True,
        },
        'uvicorn': {'propagate': True},
        'uvicorn.error': {
            'handlers': ['null'],
            'propagate': False,
        },
        'uvicorn.access': {
            'handlers': [],
            'level': logging.INFO,
            'propagate': False,
        },
        'httpx': {
            'level': logging.ERROR,
            'handlers': ['file_handler'],
            'propagate': True,
        },
    },
}
