from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtistCreateViews, ArtistListViews, ArtistRetrieveUpdateDestroyViews, ArtistDataCreateViews, ArtistDataRetrieveUpdateDestroyViews, \
                   JourneyCreateViews, JourneyRUDViews, JourneyListViews, \
                   WorkListCreateViews, WorkRUDViews, UpcomingEvents
from rest_framework.urlpatterns import format_suffix_patterns

# app_name = 'artist'

urlpatterns = [
    path('portfolios/', ArtistCreateViews.as_view()),
    path('portfolios/list/', ArtistListViews.as_view()),
    path('portfolios/<username__username>/', ArtistRetrieveUpdateDestroyViews.as_view()),
    path('bios/', ArtistDataCreateViews.as_view()),
    path('bios/<username__username>/', ArtistDataRetrieveUpdateDestroyViews.as_view()),
    path('journey/', JourneyCreateViews.as_view()),
    path('journey/<int:pk>', JourneyRUDViews.as_view()),
    path('journey/upcomingevents/', UpcomingEvents.as_view()),
    path('journey/list/', JourneyListViews.as_view()),
    path('works/', WorkListCreateViews.as_view()),
    path('works/<int:pk>', WorkRUDViews.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
