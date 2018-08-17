import string

from .models import TestCelery

from celery import shared_task

@shared_task
def update_user_clicks(user, token):
    try:
        analytics = Analytics.objects.get(token=token)
        analytics.click = analytics.click + 1
        analytics.save()

    except Analytics.DoesNotExist:
        Analytics.objects.create(user = user, token = token, click = 1)
    return 'created'
