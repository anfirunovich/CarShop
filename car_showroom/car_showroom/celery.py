import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


CELERYBEAT_SCHEDULE = {
   'buy_car_showroom': {
       'task': 'car_showroom.showroom.tasks.showroom_task',
       'schedule': crontab(minute='*/5'),
   },
   'buy_car_customer': {
     'task': 'car_showroom.customer.tasks.customer_task',
     'schedule': crontab(minute='*/2'),
  },
}