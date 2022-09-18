# db_school_hack
Скрипт предназаначен для изиенения оценок 

# Версия Python
Необходимая верисия Python3.10+

## Установка вируального окружения:  
Для Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Для Linux:  
```bash
$ python3.10 -m venv venv
$ source venv/bin/activate
```
## Устанавливаем билиотеки Python
```bash
$ pip install -r requirements.txt
```
## Необходимо создать файл .env и вставить переменные  
```bash
SECRET_KEY=<СЕКРЕТНЫЙ КЛЮЧ>
DEBUG=False
ALLOWED_HOSTS=[127.0.0.1:8000]
```
<СЕКРЕТНЫЙ КЛЮЧ> генерируется командой:
```python
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```
 
## Как использовать скрипт
```bash
$ python manage.py migrate
```
Запускаем сервер Django
```bash
$ python manage.py runserver
```
Открываем консоль ORM
```bash
$ python manage.py shell
```

В консоль `shell` вставляем скрипт из файла `scripts.py` и нажимаем Enter.  

Для исправления оценок 2 и 3 на 5 используем функцию `fix_marks()`  
Для добавления хвалебного коментария используем функцию `create_commendation(praises, '<ФИО ученика>', '<Название урока>')`  
Дата коментария будет равна дате посленего урока.


Обучающее упражнение по Django ORM от https://dvmn.org/
