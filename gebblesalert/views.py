from rest_framework import generics
# from .models import E1T1Notification, LearningsRelatedNotifications, NotificationsE1T1
from .models import NotificationsE1T1
# from .serializers import E1T1NotificationSerializers, E1T1NotificationIsSeenUpdateOnlySerializers, \
#    LearningsRelatedNotificationsSerializers, LearningsRelatedNotificationsIsSeenUpdateOnlySerializers, \
#    NotificationsE1T1Serializers, NotificationsE1T1IsSeenUpdateOnlySerializers
from .serializers import NotificationsE1T1Serializers
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

'''
class E1T1NotificationsViews(generics.ListCreateAPIView):
    serializer_class = E1T1NotificationSerializers
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        queryset = E1T1Notification.objects.all()
        receiver = self.request.query_params.get('receiver', None)  # receiver keyword goes to the URL
        if receiver is not None:
            queryset = queryset.filter(Q(receiver__username=receiver))
        return queryset


class E1T1IsSeenUpdateView(generics.RetrieveUpdateAPIView):
    queryset = E1T1Notification.objects.all()
    serializer_class = E1T1NotificationIsSeenUpdateOnlySerializers
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(receiver=self.request.user)


class LearningsNotificationsViews(generics.ListCreateAPIView):
    serializer_class = LearningsRelatedNotificationsSerializers
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        queryset = LearningsRelatedNotifications.objects.all()
        receiver = self.request.query_params.get('receiver', None)
        if receiver is not None:
            queryset = queryset.filter(receiver__username=receiver)
        return queryset


class LearningsIsSeenUpdateView(generics.RetrieveUpdateAPIView):
    queryset = LearningsRelatedNotifications.objects.all()
    serializer_class = LearningsRelatedNotificationsIsSeenUpdateOnlySerializers
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(receiver=self.request.user)
'''


class NotificationsE1T1ListCreateView(generics.ListCreateAPIView):
    queryset = NotificationsE1T1.objects.all()
    serializer_class = NotificationsE1T1Serializers
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        queryset = NotificationsE1T1.objects.all()
        receiver = self.request.query_params.get('receiver', None)
        if receiver is not None:
            # queryset = queryset.filter(receiver__username=receiver)
            queryset = queryset.filter(Q(receiver__username=receiver) | Q(receiver2__username=receiver))
        return queryset


class NotificationsE1T1IsSeenUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NotificationsE1T1.objects.all()
    serializer_class = NotificationsE1T1Serializers
    permission_classes = [IsAuthenticated, ]

# there must be something in the backend to delete the notification instances once in a while ( may be a month )
# so that the query is faster. may be we can restrict based on time stamp, query only from the notifications last month.
