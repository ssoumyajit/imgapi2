from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import E1T1NotificationsViews, E1T1IsSeenUpdateView, LearningsNotificationsViews,
#    LearningsIsSeenUpdateView, NotificationsE1T1ListCreateView, NotificationsE1T1IsSeenUpdateView
from .views import NotificationsE1T1ListCreateView, NotificationsE1T1IsSeenUpdateView

router = DefaultRouter()

app_name = 'gebblesalert'

urlpatterns = [
    path('e1t1/', NotificationsE1T1ListCreateView.as_view()),
    path('e1t1/<int:pk>', NotificationsE1T1IsSeenUpdateView.as_view()),
]

'''
path('e1t1/', E1T1NotificationsViews.as_view()),
    path('e1t1/<int:pk>', E1T1IsSeenUpdateView.as_view()),

    path('e1t1/learnings/', LearningsNotificationsViews.as_view()),
    path('e1t1/learnings/<int:pk>', LearningsIsSeenUpdateView.as_view()),
'''
