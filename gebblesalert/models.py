from django.db import models
from django.conf import settings


class E1T1Notification(models.Model):
    
    e1t1object = models.ForeignKey('sharing.Sharing', on_delete=models.CASCADE, related_name="notie1t1obj")
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifromuser")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notitouser")
    text = models.CharField(max_length=100, default='')
    time = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)
