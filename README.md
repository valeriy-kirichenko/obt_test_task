# obt_test_task
Описание проекта
----------
Тестовое задание

----------
# Установка
Стек технологий
----------
* Python 3.6
* Django 2.2
* SQLite3

Установка проекта из репозитория
----------
1. Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone 'git@github.com:valeriy-kirichenko/obt_test_task.git'
cd obt_test_task/
```
2. Cоздать и активировать виртуальное окружение:
```bash
virtualenv --python=python3.6 ~/test_venv
source ~/test_venv/bin/activate
```
3. Установить зависимости из файла ```requirements.txt```:
```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
4. Выполнить миграции:
```bash
cd m3_project/
python3 manage.py migrate
```
5. Запустить проект (в режиме сервера Django):
```bash
python3 manage.py runserver
```
----------
Автор:
----------
* **Кириченко Валерий Михайлович**
GitHub - [valeriy-kirichenko](https://github.com/valeriy-kirichenko)