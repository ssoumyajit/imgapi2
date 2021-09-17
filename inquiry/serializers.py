from rest_framework import serializers
from .models import Inquiry


class InquirySerializers(serializers.ModelSerializer):

    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)  # allow_null=False by default
    question = serializers.CharField(required=True)

    class Meta:
        model = Inquiry
        fields = ['id', 'name', 'email', 'time', 'question']