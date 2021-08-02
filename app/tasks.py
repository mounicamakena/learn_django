from celery import Celery
import time
import os
from django.core.mail import send_mail

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sample.settings')


app = Celery('tasks', broker='redis://127.0.0.1:6379/0')

@app.task
def add(x, y):
    time.sleep(1)
    return x + y


@app.task
def send_email(email):
    body = "You have been added to sample project"
    send_mail(
        'Please verify your email',
        body,
        'from@example.com',
        [email],
        fail_silently=False,
    )