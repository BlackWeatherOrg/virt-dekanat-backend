FROM python:3.12-slim

WORKDIR /project

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VIRTUALENVS_CREATE=1
ENV PYTHONPATH="${PYTHONPATH}:/project/src"

ENV TZ="Europe/Moscow"

COPY requirements.txt alembic.ini ./
COPY src src
COPY prometheus prometheus
COPY grafana grafana

RUN mkdir -p fastapi-app/logs

RUN pip install -r requirements.txt

EXPOSE 7400

CMD ["sh", "-c", "alembic upgrade head && python src/main.py"]
