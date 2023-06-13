# 1 crawling -> json data
stock_to_csv.py

# 2 json data 
json_to_sqlite.py

# 3. csv_to_sqlite
csv_to_sqlite.py




### dumpdata -UTF-8
1. EXPORT
- export PYTHONIOENCODING=utf-8
- python manage.py dumpdata > data.json

2. encoding
- python manage.py dumpdata --format=json --encoding=utf-8 > data.json

3. DATABASES
``` 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'your_db_host',
        'PORT': 'your_db_port',
        'OPTIONS': {
            'client_encoding': 'UTF8',
        },
    },
}
```
------