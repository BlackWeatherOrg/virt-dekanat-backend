import logging

import uvicorn

from settings import settings
from settings.log_config import LOGGER_CONFIG


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    uvicorn.run(
        'initializer:create_app',
        factory=True,
        log_config=LOGGER_CONFIG,
        host=settings.HOST,
        port=settings.PORT
    )


if __name__ == '__main__':
    main()
