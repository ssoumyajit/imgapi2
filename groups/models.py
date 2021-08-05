from django.db import models
from imgapiv1 import settings
# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=30)
    admin = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="groupadmin")
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Membership')

    def __str__(self):
        return self.name


# through model when we need to use some extra data with M2M relationship.
class Membership(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    # subscription attribute

