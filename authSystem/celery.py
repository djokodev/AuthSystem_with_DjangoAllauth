from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "authSystem.settings")

app = Celery("authSystem")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.update(
    broker_url=os.getenv('CELERY_BROKER_URL', 'redis://redis:6379/0'),
    result_backend=os.getenv('CELERY_RESULT_BACKEND', 'redis://redis:6379/0')
)

app.autodiscover_tasks()
