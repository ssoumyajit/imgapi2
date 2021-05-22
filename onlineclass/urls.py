from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import OnlineProgramListCreateViews, OnlineProgramRUDViews, WorkshopListCreateViews, WorkshopRUDViews, \
                   BookingCreateViews, BookingRUDViews

urlpatterns = [
    path('onlineprograms/', OnlineProgramListCreateViews.as_view()),
    path('onlineprograms/<int:pk>/', OnlineProgramRUDViews.as_view()),
    path('workshops/', WorkshopListCreateViews.as_view()),
    path('workshops/<int:pk>/', WorkshopRUDViews.as_view()),
    path('bookings/', BookingCreateViews.as_view()),
    path('bookings/<int:pk>/', BookingRUDViews.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
