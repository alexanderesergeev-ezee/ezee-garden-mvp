# ezee-garden-mvp

Репозиторий планирования MVP для практичного продукта управления садом с фокусом на Московский регион / центральную Россию.

## Что это за проект
Это концепция Python-first веб-продукта, который помогает владельцам частных участков и дач:
- наносить на карту участок и садовые зоны,
- вести простой паспорт участка,
- проверять пригодность растений,
- управлять еженедельными задачами,
- вести легкий садовый журнал.

## Текущий статус
Сейчас репозиторий находится на этапе **планирования MVP + определения scaffolding**.
Полноценный production application code на этом этапе не ожидается.

## Документы по продукту и scope
- Vision: [`docs/vision.md`](docs/vision.md)
- MVP PRD: [`docs/prd-mvp.md`](docs/prd-mvp.md)
- System requirements: [`docs/system-requirements.md`](docs/system-requirements.md)
- Milestones/backlog: [`docs/backlog.md`](docs/backlog.md)

## Планируемый стек MVP
- FastAPI
- Jinja2 templates
- Leaflet (взаимодействие с картой)
- PostgreSQL + PostGIS
- Docker Compose

## Жесткие ограничения
- Только MVP scope (держим проект простым и посильным для одного основателя).
- Без satellite-based plant recognition.
- Без заявлений о точной глубине groundwater.

## Планируемая последовательность milestones
1. **M0** docs + scaffolding
2. **M1** site + zones
3. **M2** passport + plant suitability
4. **M3** weekly tasks + journal
5. **M4** external data adapters

Подробные критерии см. в `docs/backlog.md`.

## Структура репозитория (план)
Каноничное описание структуры и архитектуры см. в `docs/system-requirements.md`.

## Быстрый старт для contributors (сейчас)
1. Прочитайте `AGENTS.md` и документы в `docs/`.
2. Соотносите любую задачу с текущим milestone scope.
3. Предпочитайте маленькие, проверяемые итерации с явными acceptance criteria.

