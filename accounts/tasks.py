
from celery import shared_task
from project.celery import Celery
import time

@shared_task
def send_build_emails(n):
    time.sleep(10)
    for x in range(n):
        print(f"sending email to {x}")
    