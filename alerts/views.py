from .models import Alert
from .serializers import AlertSerializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from permissions import IsOwnerOrReadonly
from rest_framework import generics
# from rest_framework.parsers import FormParser, MultiPartParser
from django.db.models import Q
# from rest_framework.decorators import api_view
# from rest_framework.response import Response


class AlertCreateViews(generics.CreateAPIView):
    serializer_class = AlertSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class AlertListViews(generics.ListAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        """
        filtering against queryset
        """
        queryset = Alert.objects.all()
        query = self.request.query_params.get('query', None)

        if query is not None:
            queryset = queryset.filter(Q(username__username__icontains=query))
            return queryset

        return queryset


"""
class ArtistRetrieveUpdateDestroyViews(generics.RetrieveUpdateDestroyAPIView):
    # retrieve stands for read-only endpoints to represent a single model instance.
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializers
    lookup_field = "username__username"
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadonly,)
    # parser_classes = (FormParser, MultiPartParser,)


    def perform_create(self, serializer):
        serializer.save(username=self.request.user)  # uses the id field of user object, it seems.
"""
