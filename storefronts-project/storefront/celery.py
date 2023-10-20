import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings')

celery = Celery('storefront')
celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.autodiscover_tasks()

"""
see worker command
celery -A storefront worker --loglevel=info

see beat schedule
celery -A storefront beat

monitor task using flower
celery -A storefront flower
"""
