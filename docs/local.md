# Локальное развертывание
1. Клонировать репозиторий:
```bash
git clone 'your_repo_link'
```

2. Перейти в директорию проекта:
```bash
cd your-repo
```
3. Добавить в PYTHONPATH путь до модуля app

4. Переопределить настройки через config
```bash
cp src/config/config.env.tmpl src/config/config.env
```

5. Установить poetry, если его еще нет на вашей системе (лучше почитайте официальную документацию)

6. Установить зависимости проекта с помощью poetry:
```bash
poetry install
```

7. Запустить базу данных postgres
```bash
docker-compose up --build
```

Теперь вы можете запустить сервер FastAPI:
```bash
poetry run python3 src/main.py
```