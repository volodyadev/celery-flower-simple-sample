from celery import Celery
import time

app = Celery('tasks', broker='redis://redis:6379/0')

# Добавьте эту строку для настройки повторных попыток подключения
app.conf.broker_connection_retry_on_startup = True

@app.task
def slow_fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return slow_fib(n - 1) + slow_fib(n - 2)