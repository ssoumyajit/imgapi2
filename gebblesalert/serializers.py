from rest_framework import serializers
from .models import E1T1Notification, LearningsRelatedNotifications
from user.models import User


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
        fields = ['id', 'learningobject', 'sender', 'receiver', 'notification_type', 'text', 'time', 'is_seen']


class LearningsRelatedNotificationsIsSeenUpdateOnlySerializers(serializers.ModelSerializer):

    class Meta:
        model = LearningsRelatedNotifications
        fields = ['id', 'learningobject', 'sender', 'receiver', 'notification_type', 'text', 'time', 'is_seen']
        read_only_fields = ['id', 'learningobject', 'sender', 'receiver', 'notification_type', 'text']

