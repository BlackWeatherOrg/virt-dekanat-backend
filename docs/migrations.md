# Миграции ассинхронного SQLAlchemy с помощью Alembic

## Инициализация
```bash
poetry run alembic init -t async alembic
```

## Добавление моделей
Добавлять модели нужно в target_metadata в `alembic/env.py`

Пример есть

## Автоматическая генерация миграции
Миграции хранятся в `alembic/versions`
```bash
poetry run alembic revision --autogenerate -m "Message"
```

## Ручная генерация миграции
```bash
poetry run alembic revision -m "Message"
```

## Применение последней миграции
```bash
poetry run alembic upgrade head
```

## Откат миграций
```bash
poetry run alembic downgrade base
```
Либо можно откатить до миграции по её идентификатору

## Официальная документация
Тут можно больше почитать про применение и откат миграций
https://alembic.sqlalchemy.org/en/latest/tutorial.html