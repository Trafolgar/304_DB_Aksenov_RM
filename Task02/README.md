# Лабораторная работа 2. Подготовка скриптов для создания таблиц и добавления данных

## Описание проекта

Проект реализует процесс ETL (Extract, Transform, Load) для переноса данных из текстовых файлов в базу данных SQLite. Создана кроссплатформенная утилита для автоматического создания таблиц и загрузки данных.

## Структура базы данных

База данных `movies_rating.db` содержит следующие таблицы:

### Таблица `movies`
- `id` (INTEGER PRIMARY KEY) - первичный ключ
- `title` (TEXT) - название фильма
- `year` (INTEGER) - год выпуска
- `genres` (TEXT) - жанры фильма

### Таблица `ratings`
- `id` (INTEGER PRIMARY KEY) - первичный ключ
- `user_id` (INTEGER) - идентификатор пользователя
- `movie_id` (INTEGER) - идентификатор фильма
- `rating` (REAL) - рейтинг
- `timestamp` (INTEGER) - временная метка

### Таблица `tags`
- `id` (INTEGER PRIMARY KEY) - первичный ключ
- `user_id` (INTEGER) - идентификатор пользователя
- `movie_id` (INTEGER) - идентификатор фильма
- `tag` (TEXT) - тег
- `timestamp` (INTEGER) - временная метка

### Таблица `users`
- `id` (INTEGER PRIMARY KEY) - первичный ключ
- `name` (TEXT) - имя пользователя
- `email` (TEXT) - email пользователя
- `gender` (TEXT) - пол
- `register_date` (TEXT) - дата регистрации
- `occupation` (TEXT) - род занятий

## Требования к окружению

Для корректной работы скрипта `db_init.bat` необходимо:

### Обязательные компоненты:
1. **Python 3.6 или выше**
   - Проверить установку: `python3 --version` или `python --version`
   - Скачать: https://www.python.org/downloads/

2. **SQLite 3.0 или выше**
   - Обычно предустановлен в Linux/macOS
   - Для Windows: https://www.sqlite.org/download.html
   - Проверить установку: `sqlite3 --version`

### Рекомендуемые версии:
- Python 3.8+
- SQLite 3.25+

## Структура файлов проекта
