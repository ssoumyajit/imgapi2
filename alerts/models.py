from django.db import models
from django.conf import settings


class Alert(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='alertsender', null=True, blank=False)
    areceiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='alertreceiver', null=True, blank=False)
    message = models.CharField(default='someone added you as a teacher', max_length=255)

