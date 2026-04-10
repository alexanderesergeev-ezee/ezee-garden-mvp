# MVP Backlog and Milestones

## Milestone format
Каждый milestone включает:
- Goal
- Deliverables
- Exit criteria
- Deferred items

---

## M0 — Docs and scaffolding

### Goal
Зафиксировать понятный product scope и минимальный технический scaffolding.

### Deliverables
- Финализированы Vision, PRD, system requirements и backlog.
- Базовый README для contributors.
- Начальный FastAPI project skeleton + Docker Compose + DB connectivity stub.

### Exit criteria
- Новый contributor понимает проект менее чем за 15 минут.
- `docker compose up` поднимает placeholder app и database.
- Нет business logic, кроме scaffolding.

### Deferred
- Полная auth implementation.
- Сложная frontend стилизация.

---

## M1 — Site + zones

### Goal
Пользователь может создать site и рисовать/редактировать zones на карте.

### Deliverables
- Site CRUD.
- Zone CRUD с Leaflet polygon drawing.
- Сохранение geometry в PostGIS.

### Exit criteria
- Пользователь может нарисовать минимум 2 zones и после перезагрузки данные не теряются.
- Zone attributes (sun/moisture/soil notes) редактируются.

### Deferred
- Продвинутые GIS operations.
- Mobile-first UX polish.

---

## M2 — Passport + plant suitability

### Goal
Дать практичную проверку совместимости условий участка и растений.

### Deliverables
- Форма site passport (только core fields).
- Starter plant catalog (>=20 plants).
- Rule-based suitability scoring с причинами.

### Exit criteria
- Пользователь может оценить plant для выбранной zone и увидеть “good/caution/poor” + explanation.
- При нехватке данных отображается assumption notice.

### Deferred
- ML recommendation engine.
- Automatic plant recognition.

---

## M3 — Weekly tasks + journal

### Goal
Поддержать регулярную садовую работу неделя за неделей.

### Deliverables
- Weekly task generator.
- Отслеживание статусов задач.
- Journal entries, привязанные к site/zone/plant.

### Exit criteria
- Задачи текущей недели видны и доступны для выполнения.
- Пользователь может отметить done/skipped и добавить минимум одну journal entry.

### Deferred
- Push notifications.
- Rich media management.

---

## M4 — External data adapters

### Goal
Интегрировать внешние сигналы без чрезмерного усложнения системы.

### Deliverables
- Интерфейс weather/climate adapter.
- Одна начальная provider integration.
- Базовая caching/fallback strategy.

### Exit criteria
- Логика tasks/suitability может использовать external data, когда они доступны.
- Система предсказуемо ведет себя при недоступности provider.

### Deferred
- Multiple provider arbitration.
- Real-time streaming/weather alerts.

---

## Cross-milestone quality gates
- Держать MVP scope строгим; обновлять non-goals при появлении новых запросов.
- Добавлять lightweight tests для каждого завершенного core flow.
- Сохранять простоту эксплуатации для solo founder.
