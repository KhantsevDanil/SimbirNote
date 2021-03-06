# SimbirNote
Приложение, где пользователи могут сохранять свои заметки
# Кратко о проекте
На сайте пользователи могут размещать заметки, 
На главной странице доступны все записки.
Реализована пагинация на 10 запсей. 
Запись состоит из: Автора публикации, даты, текста, возможной фотографии
и обязательного поля Тег)
#Техническое описание
Приложение реализовано на фреймворке Django.
+ Из директории backend можно развернуть проект локально
+ В папке users находится кастомная модель пользователя и всё необходимое для неё.
+ В папке notes реализованы модели Tag, Note (из которых состоят заметки). 
А так же функции создания, удаления, редактирования заметок.
+ Головная директория simbir_main содержит настройки всего приложения пагинацию и урлы
Приложение запускается из 3х контейнеров
+ db - контейнер с базой данных postgresql-alpine
+ web - контейнер содержит весь код приложения, через него идёт работа с приложением
через команды вида ``` docker-compose exec web {команда} ```
Dockerfile для жтого контейнера назодится в директории backend
+ nginx - настроенный nginx для работы с media и static
Все контейнеры описаны в директории infra
# Tag
Теги создаёт администраитор, 
пользователь может выбрать один или несколько тегов из списка, 
По средствам API реализована фильтрация по тегам. 
Это позволит пользователям легче находить заметки(
вывести только фильмы или рецепты еды
#Команды
+ запуск сайта локально из корня
``` python manage.py runserver ```
+ сбор статики
``` python manage.py collectstatic```
+ сбор миграций
``` python manage.py makemigrations```
+ активация мигаций
``` python manage.py migrate```
+ установка нужных библиотек
``` pip intall -r requirements.txt```
+ Запуск сайта локально из директории backend/
``` python manage.py runserver ```
+ Запуск сервера из ubuntu осуществляется командой
``` docker-compose up ```
+ команда для удаления базы данных и всех volumes
``` docker-compose down -v```
#API
В приложении реализована структура API
+ Документация (.yml) файл находится в директории docs.
+ Код API написан в директории backend/api 
# Инструкция по запуску проекта через докер
+ Открыть Ubuntu и Docker Desktop 
+ В Ubuntu перейти в директорию SimbirNote/infra
+ ``` docker-compose up --build```
+ ``` docker-compose exec web python manage.py makemigrations```
+ ``` docker-compose exec web python manage.py migrate```
+ ``` docker-compose exec web python manage.py runserver```
+ Проект будет открыт локально по адрессу http://127.0.0.1:8000/
# Инструкция по запуску проекта локально без докера
+ в файле SimbirNote/backend/Simbir_main/settings.py
 Изменить настройки базы данных на sqlite. 
 Для этого нужно переместить кавычки с 79-85 строки на 85-96 строку
+ ```python manage.py migrate```
+ ```python manage.py runserver```
+ Проект будет открыт локально по адрессу http://127.0.0.1:8000/
