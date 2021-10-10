from rest_framework import generics
from .models import E1T1Notification, LearningsRelatedNotifications
from .serializers import E1T1NotificationSerializers, E1T1NotificationIsSeenUpdateOnlySerializers, \
    LearningsRelatedNotificationsSerializers, LearningsRelatedNotificationsIsSeenUpdateOnlySerializers
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


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

# there must be something in the backend to delete the notification instances once in a while ( may be a month )
# so that the query is faster.
