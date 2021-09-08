from rest_framework import serializers
from .models import Alert
from user.models import User


class AlertSerializers(serializers.ModelSerializer):
    # overridden username here
    # this is where the bug is, so don can patch on Batala while updating in postman
    # username = serializers.ReadOnlyField(source='username.name')
    # username = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # HiddenField https://stackoverflow.com/questions/49557741/django-hiddenfield-value-generated-on-views
    username = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Alert
        fields = ['id', 'username', 'areceiver', 'message']
