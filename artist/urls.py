from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtistListCreateViews, ArtistRetrieveUpdateDestroyViews, ArtistDataCreateViews, ArtistDataRetrieveUpdateDestroyViews, \
                   HighlightsListCreateViews, HighlightsRUDViews, JourneyListCreateViews, JourneyRUDViews, \
                   WorkListCreateViews, WorkRUDViews
from rest_framework.urlpatterns import format_suffix_patterns

# app_name = 'artist'

urlpatterns = [
    path('portfolios/', ArtistListCreateViews.as_view()),
    path('portfolios/<username__name>/', ArtistRetrieveUpdateDestroyViews.as_view()),
    path('bios/', ArtistDataCreateViews.as_view()),
    path('bios/<username__name>/', ArtistDataRetrieveUpdateDestroyViews.as_view()),
    path('highlights/', HighlightsListCreateViews.as_view()),
    path('highlights/<int:pk>', HighlightsRUDViews.as_view()),
    path('journey/', JourneyListCreateViews.as_view()),
    path('journey/<int:pk>', JourneyRUDViews.as_view()),
    path('works/', WorkListCreateViews.as_view()),
    path('works/<int:pk>', WorkRUDViews.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
