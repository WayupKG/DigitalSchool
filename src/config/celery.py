import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config', include=['workers'])
app.config_from_object('django.conf:config', namespace='CELERY')
app.autodiscover_tasks()
app.conf.timezone = 'Asia/Bishkek'