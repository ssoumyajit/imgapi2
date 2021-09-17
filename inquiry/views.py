from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import InquirySerializers


class InquiryCreateView(generics.CreateAPIView):
    serializer_class = InquirySerializers
    permission_classes = [AllowAny,]

    # you still get the response in DRF browsable API , fix that.
    
    # def get_queryset(self):
       # return None