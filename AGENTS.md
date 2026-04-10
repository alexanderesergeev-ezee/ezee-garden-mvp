# AGENTS.md — Правила работы для `ezee-garden-mvp`

Scope: этот файл применяется ко всему репозиторию.

## Язык по умолчанию
- Язык по умолчанию для всех будущих задач — **русский**.
- Все user-facing тексты, summaries, explanations, описание задач и документация пишутся на русском.
- Не переводите имена файлов, названия технологий, имена переменных/функций/классов, API routes, SQL identifiers и CLI-команды.

## Ограничители product direction
- Этот репозиторий предназначен для **MVP planning and implementation** продукта управления садом для **Московского региона / центральной России**.
- Scope должен оставаться практичным для реализации и поддержки **одним основателем**.
- Приоритет: понятные документы, маленькие итерации и доставка результата, а не архитектурная избыточность.

## Hard constraints
- Не добавляйте speculative/research-heavy функции без явного запроса.
- Не вводите satellite-based plant recognition.
- Не заявляйте точные значения глубины groundwater; допускаются только proxy-индикаторы и confidence notes.
- Архитектура должна оставаться **Python-first**.
- Предпочтительный stack для MVP:
  - FastAPI
  - Jinja2 templates
  - Leaflet (map UI)
  - PostgreSQL + PostGIS
  - Docker Compose

## Scope discipline
- Реализуйте только то, что нужно для acceptance criteria текущего milestone.
- Предпочитайте default/simple решения до введения абстракций.
- Избегайте раннего внедрения microservices, Kubernetes, event buses и сложного CI/CD.
- Любая новая dependency должна сопровождаться однострочным обоснованием.

## Ожидания по документации
При обновлении product docs (`docs/*.md`, `README.md`):
- Формулировки должны быть конкретными и проверяемыми.
- Явно разделяйте **MVP scope** и **non-goals**.
- По возможности используйте checklists и acceptance criteria.
- Явно фиксируйте assumptions и open questions.

## Ожидания по коду (когда начнется code work)
- Держите модули небольшими и связными.
- Пишите прямолинейный код на SQLAlchemy/Alembic/FastAPI.
- Добавляйте минимальные тесты для core flows до вторичных функций.
- Предпочитайте server-rendered UX на Jinja2 вместо усложнения SPA.

## Definition of done для задач
Задача считается завершенной только если:
1. Обновлены релевантные документы.
2. Scope и non-goals остаются явными.
3. Команды/тесты (если есть) задокументированы в результате задачи.
4. Follow-up работа зафиксирована в `docs/backlog.md`.
