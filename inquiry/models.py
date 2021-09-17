# import for creating a inquiry model
from django.db import models
from datetime import date


class Inquiry(models.Model):
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, blank=False)
    question = models.TextField()
    time = models.DateTimeField(auto_now_add=True)  # blank=True set by default, check docs.