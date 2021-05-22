from django.db import models
from django.conf import settings


class OnlineProgram(models.Model):
    username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="onlineprogram", blank=False)
    title = models.CharField(max_length=255, default="", blank=True)
    about = models.TextField(default="", blank=True)

    def __str__(self):
        return self.username


class Workshop(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="workshop", blank=False)
    title = models.CharField(max_length=255, default="", blank=True)
    schedule = models.DateTimeField(null=True, blank=True)
    rules = models.TextField(default="", blank=True)
    extrainfo = models.TextField(default="", blank=True)
    paymentlink = models.URLField(max_length=200, default="", blank=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="booking", blank=False)
    workshop = models.ForeignKey('Workshop', on_delete=models.CASCADE, blank=False, related_name="applicants")
    text = models.TextField(default="", blank=True)
    # emailreceived = boolean


# ask a question before booking option.
# print a pdf for the teacher with all details.


