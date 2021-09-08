from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlertCreateViews, AlertListViews
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'alerts'

urlpatterns = [
    path('create/', AlertCreateViews.as_view()),
    path('list/', AlertListViews.as_view()),
    # path('portfolios/<username__username>/', ArtistRetrieveUpdateDestroyViews.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
