from celery import Celery
import time
import os
from django.core.mail import send_mail
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage

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


@app.task
def send_email_with_template(email):
    body = "You have been added to sample project"
    template = "employee_mail.html"

    ctx = {
        'user': email
    }
    message = get_template(template).render(ctx)
    msg = EmailMessage(
        'Subject',
        message,
        'from@example.com',
        [email],
    )
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()
    print("Mail successfully sent")
    

@app.task
def send_email_with_template_attachment(email):
    body = "You have been added to sample project"
    template = "employee_mail.html"

    ctx = {
        'user': email
    }
    message = get_template(template).render(ctx)
    msg = EmailMessage(
        'Subject',
        message,
        'from@example.com',
        [email],
    )
    msg.attach_file("movies.rtf")
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()
    print("Mail successfully sent")
       