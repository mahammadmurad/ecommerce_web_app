import os

from celery import Celery

from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

app = Celery('ecommerce')


app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule = {
    "cron": {
        
        "task": "app.tasks.delete_db",
        "schedule": crontab(minute="*")
        
        }
}

app.autodiscover_tasks()
