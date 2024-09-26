# News Parser Project

## Описание
Этот проект представляет собой парсер новостей с сайта **Hacker News**. Программа написана на Python и использует библиотеки `requests` 
и `BeautifulSoup` для сбора данных, а также `MySQL` для сохранения результатов.

Парсер собирает заголовки, ссылки и количество очков (рейтинг) новостей с главной страницы Hacker News и сохраняет их в базу данных.

## Установка и запуск

### 1. Клонирование репозитория
```bash
git clone https://github.com/enpure/news_parser.git
cd news_parser

### 2. Установка виртуальной среды и зависимостей
```bash
python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
pip install -r requirements.txt

### 3. Настройка базы данных
```bash
Создайте базу данных MySQL и таблицу для хранения новостей (см. файл db.py для структуры).

### 4. Запуск парсера
```bash
python main.py

### Используемые технологии
Python
BeautifulSoup
Requests
MySQL

### Задачи
Парсинг новостей с сайта Hacker News
Сохранение данных в MySQL
Возможность расширения для парсинга других сайтов

### Автор
enpure
