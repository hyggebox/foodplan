# Сайт, где можно каждый день получить новые рецепты на день.
Интернет сайт на основе Django
[![Python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
## Описание
*Проект не закончен.*

Сервис, предоставляющий каждый день, во время действия подписки случайные рецепт(ы) исходя из ограничений пользователя

## Как установить
 - Склонировать проект
```shell
git clone https://github.com/hyggebox/foodplan.git
```
 - Установить requirements.txt
```shell
pip install -r requirements.txt
```
 - Создать файл .env и заполнить в нем переменные:

```dotenv
DEBUG='дебаг-режим. Поставьте `True` для включения, `False` -- для 
выключения отладочного режима. По умолчанию дебаг-режим отключен'
```
```dotenv
SECRET_KEY='секретный ключ проекта'
```
```dotenv
ALLOWED_HOSTS='Список разрешенных хостов'
```

## Цель проекта
Код написан в рамках самостоятельного проекта на онлайн-курсе для веб-разработчиков [Devman](https://dvmn.org).