# ezee-garden-mvp

Репозиторий MVP для продукта управления садом с фокусом на Московский регион / центральную Россию.

## Что уже реализовано (M0 scaffolding)
- Минимальное FastAPI-приложение с entrypoint `app/main.py`.
- Web-роут `/` на Jinja2 templates.
- API health endpoint `GET /api/health`.
- Базовый шаблон и простая главная страница.
- Leaflet-карта в демо-режиме (минимальный JavaScript).
- Docker Compose для `app` + `db` (PostgreSQL + PostGIS).
- Базовый тест на health endpoint (`pytest`).
- Настроены `ruff` и зависимости через `pyproject.toml`.

## Текущий стек
- FastAPI
- Jinja2 templates
- минимальный JavaScript
- Leaflet
- PostgreSQL + PostGIS
- Docker Compose
- pytest
- ruff

## Структура проекта
```text
.
├── app/
│   ├── main.py
│   ├── web/
│   ├── api/
│   ├── templates/
│   ├── static/
│   ├── domain/
│   │   ├── models/
│   │   ├── services/
│   │   └── rules/
│   ├── adapters/
│   └── db/
├── docs/
├── tests/
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
└── .env.example
```

## Быстрый запуск
1. Создайте `.env` из примера:
   ```bash
   cp .env.example .env
   ```
2. Запустите контейнеры:
   ```bash
   docker compose up --build
   ```
3. Откройте приложение:
   - Главная страница: http://localhost:8000/
   - Health: http://localhost:8000/api/health

## Локальный запуск без Docker
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
uvicorn app.main:app --reload
```

## Проверки
```bash
ruff check .
pytest
```

## Документация
- Правила работы: `AGENTS.md`
- Vision: `docs/vision.md`
- PRD: `docs/prd-mvp.md`
- System requirements: `docs/system-requirements.md`
- Backlog: `docs/backlog.md`

## Ограничения текущего этапа
- Без authentication.
- Без внешних API.
- Без plant suitability.
- Без geodata adapters.
- Без сложного frontend framework.
