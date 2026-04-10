# PRD — MVP

## 1) Target user
Primary user:
- Владелец дома / дачи в Московском регионе или центральной России.
- Поддерживает небольшой или средний участок (примерно 4–30 соток).
- Ищет структурированное планирование и еженедельные подсказки, а не agronomic deep-tech.

Secondary early user:
- Член семьи, который помогает с сезонным планированием и отслеживанием задач.

## 2) MVP scope
MVP включает четыре ключевые возможности:

1. **Site and zones**
   - Создать один site.
   - Рисовать/редактировать garden zones на карте (Leaflet polygons).
   - Хранить zone attributes: инсоляция, базовая склонность к влажности, заметки по почве.

2. **Site passport + plant suitability**
   - Вести практичные поля site passport (без требований к лабораторной точности).
   - Добавлять растения из curated starter catalog.
   - Показывать уровень suitability по каждой zone (good / caution / poor) с причинами.

3. **Weekly tasks**
   - Генерировать weekly to-do list на основе сезона + zone + профиля растения.
   - Отслеживать статус задач (todo / done / skipped).

4. **Journal**
   - Добавлять dated text notes по site/zone/plant.
   - Опционально хранить image link metadata (URL/path), без тяжелого media pipeline в MVP.

## 3) Non-goals (явно вне MVP)
- Satellite-based plant recognition.
- Определение точной глубины groundwater.
- Автономное управление оборудованием irrigation.
- Marketplace/e-commerce.
- Social feed/community features.
- Продвинутая AI-диагностика по фото.
- Multi-region agronomic optimization за пределами Moscow-region-first правил.

## 4) Core user flows

### Flow A — First-time setup
1. User signs in.
2. Создает site.
3. Открывает карту, рисует 2+ zones.
4. Заполняет минимальные значения passport.

**Expected outcome:** пользователь получает рабочую цифровую карту и базовые условия участка.

### Flow B — Plant planning
1. Пользователь выбирает zone.
2. Добавляет candidate plant из catalog.
3. Система возвращает suitability с коротким объяснением.

**Expected outcome:** пользователь быстро отсеивает неудачные варианты и оставляет подходящие.

### Flow C — Weekly routine
1. Пользователь еженедельно открывает dashboard.
2. Просматривает сгенерированные tasks.
3. Отмечает done/skipped.
4. Добавляет краткую journal note по важным наблюдениям.

**Expected outcome:** повторяемый сезонный процесс с видимым прогрессом.

## 5) Acceptance criteria

### Functional
- Пользователь может создавать/редактировать/удалять одну или несколько zones на карте.
- Zone geometry и attributes сохраняются в PostGIS.
- Пользователь может create/read/update site passport.
- Suitability response формируется как минимум для 20 starter plants.
- Weekly tasks генерируются для текущей недели и поддерживают обновление статуса.
- Journal поддерживает CRUD для text notes с датой и привязкой к контексту.

### UX
- Основные flows работают на desktop без сложности frontend build (Jinja2 server-rendered pages).
- Любая suitability/task recommendation содержит короткое «почему».

### Reliability
- `docker compose up` поднимает app + db локально.
- Базовый health endpoint возвращает OK.
- Критичная DB schema управляется через migrations.

### Delivery constraints
- Реализация остается достаточно компактной для solo maintainer.
- Для решений MVP предпочтительны явные правила вместо непрозрачного ML.
