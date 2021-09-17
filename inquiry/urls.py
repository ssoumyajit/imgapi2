from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import InquiryCreateView

urlpatterns = [
    path('', InquiryCreateView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)