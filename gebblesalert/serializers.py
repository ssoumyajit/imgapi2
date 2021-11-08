from rest_framework import serializers
# from .models import E1T1Notification, LearningsRelatedNotifications, NotificationsE1T1
from .models import NotificationsE1T1
from sharing.models import Learnings, SharingMessage
from user.models import User

'''
class E1T1NotificationSerializers(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username', required=True, allow_null=True)
    receiver = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username', required=True, allow_null=True)

    class Meta:
        model = E1T1Notification
        fields = ['id', 'e1t1object', 'sender', 'receiver', 'notification_type', 'text', 'time', 'is_seen']


# create a serializer to keep every attribute except is_seen read_only.
# because otherwise a user can change the e1t1 object id. such a serious bug.
class E1T1NotificationIsSeenUpdateOnlySerializers(serializers.ModelSerializer):

    class Meta:
        model = E1T1Notification
        fields = ['id', 'e1t1object', 'sender', 'receiver', 'notification_type', 'text', 'time', 'is_seen']
        read_only_fields = ['id', 'e1t1object', 'sender', 'receiver', 'notification_type', 'text']


class LearningsRelatedNotificationsSerializers(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username', required=True,
                                          allow_null=True)
    receiver = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username', required=True,
                                            allow_null=True)

    class Meta:
        model = LearningsRelatedNotifications
        fields = ['id', 'e1t1object', 'learningobject', 'sender', 'receiver', 'notification_type', 'text', 'time', 'is_seen']


class LearningsRelatedNotificationsIsSeenUpdateOnlySerializers(serializers.ModelSerializer):

    class Meta:
        model = LearningsRelatedNotifications
        fields = ['id', 'e1t1object', 'learningobject', 'sender', 'receiver', 'notification_type', 'text', 'time', 'is_seen']
        read_only_fields = ['id', 'e1t1object', 'learningobject', 'sender', 'receiver', 'notification_type', 'text']
'''


class NotificationsE1T1Serializers(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username', required=True,
                                          allow_null=True)
    receiver = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username', required=True,
                                            allow_null=True)
    # e1t1object = serializers.PrimaryKeyRelatedField(queryset=Sharing.objects.all())
    learningobject = serializers.PrimaryKeyRelatedField(queryset=Learnings.objects.all(), required=False, allow_null=True)
    # can I still filter it based, which E1T1 instance !!
    chatobject = serializers.PrimaryKeyRelatedField(queryset=SharingMessage.objects.all(), required=False, allow_null=True)
    # since u put require false, make sure frontend handles this segregation

    # Write a serializer validation based on which E1T1 instance:
    class Meta:
        model = NotificationsE1T1
        fields = ['id', 'e1t1object', 'learningobject', 'chatobject', 'sender', 'receiver', 'notification_type',
                  'notification_context', 'text', 'time', 'is_seen']


class NotificationsE1T1IsSeenUpdateOnlySerializers(serializers.ModelSerializer):

    class Meta:
        model = NotificationsE1T1
        fields = ['id', 'e1t1object', 'learningobject', 'chatobject', 'sender', 'receiver', 'notification_type',
                  'notification_context', 'text', 'time', 'is_seen']
        read_only_fields = ['id', 'e1t1object', 'learningobject', 'chatobject', 'sender', 'receiver', 'notification_type',
                  'notification_context', 'text']

