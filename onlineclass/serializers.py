from rest_framework import serializers
from .models import OnlineProgram, Workshop, Booking
from user.models import User


class OnlineProgramSerializers(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = OnlineProgram
        fields = "__all__"


class BookingSerializers(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Booking
        fields = "__all__"


class WorkshopSerializers(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
    applicants = BookingSerializers(many=True, read_only=True)

    class Meta:
        model = Workshop
        fields = ['username', 'title', 'rules', 'extrainfo', 'paymentlink', 'applicants']
        depth = 1
        # exclude = ('schedule',)