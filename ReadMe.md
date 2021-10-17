# Survey API

Создает опросники по АПИ.


## Installation


```bash
git clone  https://github.com/apollo64/opros.githtm
pip install -r requirements.txt
```

## Usage

```python
python manage.py runserver 8000

# Отобразить список текущих опросников , создать новый опрос (в браузере в адресной строке)
localhost:8000/api/surveys

# Отобразить вопросы опроса и редактировать сам опрос
localhost:8000/api/survey/pk/

# Отобразить список ответов на конкретный вопрос и редактировать сам вопрос (question_pk), добавить новые варианты ответов 
localhost:8000/api/question/question_pk/

# Создать новый вариант ответа для конкретного вопроса (question_pk), добавить новые варианты ответов 
localhost:8000/api/question/question_pk/

# Отобразить детали варианта ответа - редактировать, удалить 
localhost:8000/api/option/pk/

# Отобразить отобразить список опросов для анонимных пользователей
localhost:8000/

# Отобразить отобразить вопрос опроса, заполнить
localhost:8000/survey/pk/

# Отобразить отобразить список опросов для анонимных пользователей
localhost:8000/ 

# Ответить на вопрос опроса
localhost:8000/answer/pk

# Посмотреть ответы пользователя
localhost:8000/result/pk
```
