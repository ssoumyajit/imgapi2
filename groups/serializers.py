from rest_framework import serializers
from .models import Group
from user.models import User


class GroupSerializer(serializers.ModelSerializer):
    admin = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='admin')

    class Meta:
        model = Group
        fields = ['name', 'admin', 'members']
