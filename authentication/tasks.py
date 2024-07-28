from celery import shared_task
import time


@shared_task
def test_task():
    print("Hello World")
    time.sleep(5)
    return "Task completed successfully"
