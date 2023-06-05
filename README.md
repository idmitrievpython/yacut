# YaCut
Сервис укорачивания ссылок с web интерфейсом и REST API. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

## Содержание
- [Технологии](#технологии)
- [Использование](#использование)
- [REST API](#rest-api)
- [Над проектом работали](#над-проектом-работали)

## Технологии
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [Jinja](https://jinja.palletsprojects.com/)
- [Flask-WTF](https://flask-wtf.readthedocs.io/)
- [Flask-Migrate](https://flask-migrate.readthedocs.io/)

## Использование
Склонируйте репозиторий  
Создайте виртуальное окружение 
```
python -m venv venv
```
Активируйте виртуальное окружение  
Установите зависимости 
```
pip install -r requirements.txt
```
Примените миграции
```
flask db upgrade
```
Запустите сервер
```
flask run
```
web интервейс будет доступен по адресу http://localhost:5000/

## REST API
Документация по API: 

## Над проектом работал
- [Илья Дмитриев]