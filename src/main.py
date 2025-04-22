import uvicorn

from settings import settings


def main():
    uvicorn.run(
        'initialize:create_app',
        factory=True,
        host=settings.HOST,
        port=settings.PORT
    )


if __name__ == '__main__':
    main()