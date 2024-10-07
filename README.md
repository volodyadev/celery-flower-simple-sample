# Запуск проекта

Для запуска проекта используйте следующую команду:

```bash
docker-compose up --build
```

# Создание задачи


Для подключения к контейнеру выполните команду:

```bash

docker exec -it celery-celery-1 python
```


Внутри контейнера создайте задачу следующим образом:

```python

from tasks import slow_fib
result = slow_fib.delay(30)
```

# Отслeживаем задачи

http://localhost:5555/tasks