from rest_framework import serializers
from .models import E1T1Notification
from user.models import User


class E1T1NotificationSerializers(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username', required=True, allow_null=True)
    receiver = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username', required=True, allow_null=True)

    class Meta:
        model = E1T1Notification
        fields = ['id', 'e1t1object', 'sender', 'receiver', 'text', 'time', 'is_seen']
