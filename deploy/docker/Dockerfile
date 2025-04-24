FROM python:3.12-slim

WORKDIR /project

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VIRTUALENVS_CREATE=1
ENV PYTHONPATH="${PYTHONPATH}:/project/src"

ENV TZ="Europe/Moscow"

RUN pip install poetry

COPY pyproject.toml alembic.ini ./
COPY src src

RUN poetry install

EXPOSE 7400

CMD ["sh", "-c", "poetry run alembic upgrade head && poetry run python src/main.py"]
