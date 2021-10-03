from rest_framework import generics
from .models import E1T1Notification
from .serializers import E1T1NotificationSerializers, E1T1NotificationIsSeenUpdateOnlySerializers
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
