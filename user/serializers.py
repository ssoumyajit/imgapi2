from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from user.models import GENDER_SELECTION, User
# from django_countries.serializers import CountryFieldMixin
from django_countries.serializer_fields import CountryField  # for low level usage


class CustomRegisterSerializer(RegisterSerializer):
    gender = serializers.ChoiceField(choices=GENDER_SELECTION)
    country = CountryField()

    # Define transaction.atomic to rollback the save operation in case of error
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.gender = self.data.get('gender')
        user.country = self.data.get('country')
        user.save()
        return user


class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'pk',
            'email',
            'gender',
            'username',
            'country'
        )
        read_only_fields = ('pk', 'email', 'gender', 'username', 'country')















"""
from django.contrib.auth import get_user_model, authenticate
from rest_framework.serializers import ModelSerializer
from .models import User
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django_countries.serializers import CountryFieldMixin
from django_countries.serializer_fields import CountryField


# https://github.com/SmileyChris/django-countries
# https://github.com/SmileyChris/django-countries/issues/106
# https://stackoverflow.com/questions/40669313/django-countries-in-django-rest-framework
"""

"""
class UserSerializer(ModelSerializer):
    # serializer for users object

    # country = CountryField()
    class Meta:
        model = get_user_model()  # return the use model that is active in this project
        # model = User
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        # create a new user with encrypted password and return it
        # basically overwrites the create function provided by base user class \
        #   and uses our custom user model
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):

        # update a user, setting the password correctly and return it.

        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class CustomTokenSerializer(TokenObtainPairSerializer):

    # Provides user details along with tokens

    def validate(self, attrs):
        # default result (access/refresh tokens)
        data = super(CustomTokenSerializer, self).validate(attrs)
        # custom data you want to include
        data.update({'username': self.user.name})
        data.update({'id': self.user.id})
        # data.update({'country': self.user.country})
        return data


class AuthTokenSerializer(serializers.Serializer):

    # serializer for user authentication object.

    email = serializers.CharField()
    password = serializers.CharField(
        style = {'input_type': 'password'},
        trim_whitespace = False
    )
    # username

    def validate(self, attrs):

        # validate and authenticate the user

        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request = self.context.get('request'),
            username = email,
            password = password
        )
        if not user:
            msg = _('unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code = 'authorization')
        attrs['user'] = user
        return attrs
        # you always return the object at the end of the validation.
"""

