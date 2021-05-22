from django.shortcuts import render
from .models import OnlineProgram, Workshop, Booking
from .serializers import OnlineProgramSerializers, WorkshopSerializers, BookingSerializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from permissions import IsOwnerOrReadonly
from rest_framework import generics


class OnlineProgramListCreateViews(generics.ListCreateAPIView):
    queryset = OnlineProgram.objects.all()
    serializer_class = OnlineProgramSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        """
        filtering against queryset
        # *** check another way to do it based on request.user
        """
        queryset = OnlineProgram.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username__name=username)
        return queryset


class OnlineProgramRUDViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = OnlineProgram.objects.all()
    serializer_class = OnlineProgramSerializers
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadonly,)

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)


class WorkshopListCreateViews(generics.ListCreateAPIView):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class WorkshopRUDViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializers
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadonly,)

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)


class BookingCreateViews(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class BookingRUDViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadonly,)

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)


