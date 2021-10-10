from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import E1T1NotificationsViews, E1T1IsSeenUpdateView, LearningsNotificationsViews, LearningsIsSeenUpdateView

router = DefaultRouter()

app_name = 'gebblesalert'

urlpatterns = [
    path('', E1T1NotificationsViews.as_view()),
    path('<int:pk>', E1T1IsSeenUpdateView.as_view()),

    path('e1t1/learnings/', LearningsNotificationsViews.as_view()),
    path('e1t1/learnings/<int:pk>', LearningsIsSeenUpdateView.as_view()),
]

