from django.db import models

from django.db import models
from django.conf import settings
from user.models import User
from django_countries.fields import CountryField
import time
import datetime
import uuid


class Sharing(models.Model):
    # SHARING starts with the student.

    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="student")
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="teacher", 
    null=True, blank=True)
    s_teacher_name = models.CharField(default="", max_length=255)
    s_teacher_country = CountryField(default="", blank=True)
    s_student_country = CountryField(default="", blank=True)
    s_photo = models.ImageField(default="", upload_to="sharing/")
    s_appreciation = models.TextField(default="")  # 1 line = 8 words, 20 lines to cover up the image
    s_learnings = models.TextField(default="")
    s_video_talk = models.FileField(default="", upload_to="talk/")
    s_video_dance = models.FileField(default="", upload_to="dance/")
    s_date = models.DateField(auto_now=True)  # keeping track of the user's posting time.
    s_location = models.CharField(max_length=255,)
    s_teacher_video = models.URLField(default="", max_length=255, blank=True)

    # voters_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = "votes")

    class Meta:
        ordering = ['s_date']


class LikesToSharing(models.Model):
    LOVE = 'LO'
    DOPE = 'DO'
    INSPIRING = 'IS'
    RESPECT = 'RS'
    CUTE = 'CT'
    INFORMATIVE = 'IF'
    EMOTIONAL = 'EM'

    HOW_YOU_LIKE_IT_CHOICES = [
        (LOVE, 'love'),
        (DOPE, 'dope'),
        (INSPIRING, 'inspiring'),
        (RESPECT, 'respect'),
        (CUTE, 'cute'),
        (INFORMATIVE, 'informative'),
        (EMOTIONAL, 'emotional'),
    ]

    l_shareid = models.ForeignKey('Sharing', on_delete=models.CASCADE, related_name="likes_sharing")
    l_liker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    l_type = models.CharField(
        max_length=2,
        choices=HOW_YOU_LIKE_IT_CHOICES,
        default=LOVE
    )


class Comments(models.Model):
    c_shareid = models.ForeignKey('Sharing', on_delete=models.CASCADE, related_name="comments_sharing")
    c_commenter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    c_comment = models.TextField(default="")  # add a validation here.
    c_time = models.DateTimeField(auto_now=True)
    # may be here just a like option embedded directly, no types of like.


# class SharingMessage(models.Model):
#     pass
    # username = fk (User)     : view > if request.user -> MessagePermission (True)
    # shareid = fk (Sharing)   # : add validation on serializer based on username and trim down the options ( one user has few shares only )
    # add frontend validation: automatically add shareid, coz u r in detail page.
    # messagetext = charfield

class SharingMessage(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="qna", null = True)
    shareid = models.ForeignKey('Sharing', on_delete=models.CASCADE, related_name="qnaid", null= True)
    messagetext = models.TextField(default='')
    created = models.DateTimeField(auto_now=True)

