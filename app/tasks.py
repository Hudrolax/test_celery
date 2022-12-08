from time import sleep
from celery import Celery

app = Celery('tasks', backend='redis://redis', broker='redis://redis')


@app.task
def add(x, y):
    sleep(3)
    return x + y
