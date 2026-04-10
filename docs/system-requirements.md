# System Requirements (MVP)

## 1) Architecture overview
Python-first monolith с server-rendered web UI.

- **Backend/Web:** FastAPI
- **Templates:** Jinja2
- **Map UI:** Leaflet (встроен в Jinja2 pages)
- **Database:** PostgreSQL + PostGIS
- **Runtime:** Docker Compose (app + db)

Эта архитектура намеренно простая и подходит для одного основателя.

## 2) High-level components

1. **Web App (FastAPI)**
   - Auth/session handling (простой email/password или invite-based login для MVP).
   - HTML endpoints для dashboard, site, zones, plants, tasks, journal.
   - JSON endpoints для map geometry и динамических действий UI.

2. **Rules Engine (in-process module)**
   - Детерминированный suitability scoring по данным zone/passport + plant requirements.
   - Детерминированная генерация weekly tasks по сезону + plant/stage data.

3. **PostgreSQL/PostGIS**
   - Хранит users, sites, zones, geometries, plants, suitability results, tasks, journal.

4. **External Adapters (M4)**
   - Источники weather/calendar/climate через тонкие adapter interfaces.
   - Fail-soft поведение: cached/default режим при недоступности provider.

## 3) Functional requirements
- Поддержка связи one-to-many: user → sites → zones.
- Хранение и запрос zone polygons как PostGIS geometry.
- Сохранение passport inputs и plant requirements.
- Расчет и отображение suitability с объяснимыми причинами.
- Генерация weekly task lists и отслеживание статусов.
- Ведение dated journal entries.

## 4) Non-functional requirements
- Локальный запуск разработки менее чем за 10 минут на чистой машине (с установленным Docker).
- Цель по P95 для core pages: < 800ms в локальном/небольшом развертывании.
- Стратегия ежедневного automated DB backup должна быть определена до production pilot.
- Логи должны быть достаточными для отладки task generation и suitability decisions.

## 5) Proposed repository structure

```text
.
├── app/
│   ├── main.py                  # FastAPI app entry
│   ├── web/                     # Jinja routes/controllers
│   ├── api/                     # JSON endpoints
│   ├── templates/               # Jinja2 templates
│   ├── static/                  # CSS/JS assets (including Leaflet integration)
│   ├── domain/
│   │   ├── models/              # ORM models
│   │   ├── services/            # site/passport/tasks/journal logic
│   │   └── rules/               # suitability + weekly planner rules
│   ├── adapters/                # external providers (weather, etc.)
│   └── db/
│       ├── session.py
│       └── migrations/          # Alembic
├── docs/
│   ├── vision.md
│   ├── prd-mvp.md
│   ├── system-requirements.md
│   └── backlog.md
├── tests/
│   ├── unit/
│   └── integration/
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
└── README.md
```

## 6) Technology requirements
- Python 3.12+
- FastAPI
- Jinja2
- SQLAlchemy + Alembic
- psycopg (или asyncpg, если выбран async stack)
- PostgreSQL 15+ с PostGIS extension
- Leaflet (CDN или vendored static assets)

## 7) Data and domain constraints
- Все агрономические результаты носят advisory-характер и не гарантируют итог.
- Без заявлений о точной глубине groundwater.
- Suitability outputs должны показывать confidence/assumption notes при неполных данных.
- Geography rules в MVP приоритизируют условия Московского региона.
