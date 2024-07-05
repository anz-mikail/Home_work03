import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HW_03.settings')

app = Celery('HW_03')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'action_every_monday_8am': {
        'task': 'news.tasks.send_mail_weekly',
        'schedule': crontab(hour=08, minute=00, day_of_week='monday'),
        'args':()
    }
}

