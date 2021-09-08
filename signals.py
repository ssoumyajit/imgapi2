from django.db.models.signals import post_save
from notifications.signals import notify
from alerts.models import Alert


def my_handler(sender, instance, created, **kwargs):
    notify.send(instance, verb='tagged you as teacher')


post_save.connect(my_handler, sender=Alert)
