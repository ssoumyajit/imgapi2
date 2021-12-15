from django.db import models
from django.conf import settings

# Categorize the notifications based on the data Model.
# for example, there will be notifications for likes, comments and update to
# every learning instance. Hence just keep a notification_type variable to
# mark them.

# related_name should be in plural. coz it always returns multiple values !!

'''
class E1T1Notification(models.Model):
    NOTIFICATION_TYPES = ((1, 'Love'), (2, 'Comment'), (3, 'e1t1_creation'))
    
    e1t1object = models.ForeignKey('sharing.Sharing', on_delete=models.CASCADE, related_name="notie1t1obj")
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifromuser")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notitouser")
    text = models.CharField(max_length=100, default='')
    time = models.DateTimeField(auto_now_add=True)
    notification_type = models.IntegerField(choices=NOTIFICATION_TYPES)  # added later, so migrate again
    is_seen = models.BooleanField(default=False)


class LearningsRelatedNotifications(models.Model):
    NOTIFICATION_TYPES = ((1, 'Like'), (2, 'Comment'), (3, 'learning_creation'))

    e1t1object = models.ForeignKey('sharing.Sharing', on_delete=models.CASCADE, related_name="e1t1objectoflearning")
    learningobject = models.ForeignKey('sharing.Learnings', on_delete=models.CASCADE, related_name="notilearningobj")
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifromuser_learning_like_comment")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notitouser_learning_like_comment")
    text = models.CharField(max_length=100, default='')
    time = models.DateTimeField(auto_now_add=True)
    notification_type = models.IntegerField(choices=NOTIFICATION_TYPES)
    is_seen = models.BooleanField(default=False)
'''


class NotificationsE1T1(models.Model):
    NOTIFICATION_CONTEXTS = ((1, 'e1t1'), (2, 'learnings'), (3, 'private_messages'))
    NOTIFICATION_TYPES = ((1, 'creation'), (2, 'like'), (3, 'comment'))  # what kind of like resides in corresponding Like model'), (2, 'like'), (3, ''))  # what kind of like residing in corresponding Like model

    e1t1object = models.ForeignKey('sharing.Sharing', on_delete=models.CASCADE, related_name="notie1t1object")  # mandatory

    learningobject = models.ForeignKey('sharing.Learnings', on_delete=models.CASCADE, related_name="notilearningobject", null=True, blank=False)
    chatobject = models.ForeignKey('sharing.SharingMessage', on_delete=models.CASCADE, related_name="notichatobject", null=True, blank=False)

    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifromuserobject")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notitouserobject")
    receiver2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notitouser2object", null=True)  # null=True coz
    # for Private Chat, we do not send the notification back to the writer whoever it might be; teacher or student !!

    text = models.CharField(max_length=100, default='')
    time = models.DateTimeField(auto_now_add=True)
    notification_context = models.IntegerField(choices=NOTIFICATION_CONTEXTS)
    notification_type = models.IntegerField(choices=NOTIFICATION_TYPES)  # added later, so migrate again
    is_seen = models.BooleanField(default=False)



