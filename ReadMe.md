# Survey API

Создает опросники по АПИ.


## Installation


```bash
git clone 
pip install -r requirements.txt
```

## Usage

```python
python manage.py runserver 8000

# Отобразить список текущих опросников (в браузере в адресной строке)
localhost:8000/api/surveys

# Отобразить вопросы и добавить новые
localhost:8000/api/survey/pk/questions

# Отобразить список ответов на конкретный вопрос (question_pk), добавить новые варианты ответов 
localhost:8000/api/question/question_pk/options

# Отобразить детали вопроса - редактировать, удалить 
localhost:8000/api/question/pk/

# Отобразить детали варианта ответа - редактировать, удалить 
localhost:8000/api/option/pk/

```
