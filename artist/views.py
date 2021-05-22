from django.shortcuts import render
from .models import Artist, ArtistData, Highlights, Journey
from .serializers import ArtistSerializers, ArtistDataSerializers, HighlightsSerializers, JourneySerializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import permissions
from rest_framework import filters
from rest_framework_simplejwt.authentication import JWTAuthentication
from permissions import IsOwnerOrReadonly
from rest_framework import generics
# from rest_framework.parsers import FormParser, MultiPartParser


class ArtistListCreateViews(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


    # filtering which artists to be shown
    # may be filter using dance style, teachers later
    """
        def get_queryset(self):
        # Filter active products
            return Product.objects.filter(active=True)
    """


class ArtistRetrieveUpdateDestroyViews(generics.RetrieveUpdateDestroyAPIView):
    # retrieve stands for read-only endpoints to represent a single model instance.
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializers
    lookup_field = "username__name"
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadonly,)
    # parser_classes = (FormParser, MultiPartParser,)
    
    """
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(ArtistSerializers, self).__init__(*args, **kwargs)
    """
    """
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
    """
    

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)   # uses the id field of user object, it seems.


class ArtistDataCreateViews(generics.CreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistDataSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ArtistDataRetrieveUpdateDestroyViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArtistData.objects.all()
    serializer_class = ArtistDataSerializers
    lookup_field = 'username__name'
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadonly,)

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)


class HighlightsListCreateViews(generics.ListCreateAPIView):
    queryset = Highlights.objects.all()
    serializer_class = HighlightsSerializers
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['username__name']
    # authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # just use explicit queryset n filter

    def get_queryset(self):
        """
        filtering against queryset
        """
        queryset = Highlights.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username__name=username)
        return queryset


class HighlightsRUDViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Highlights.objects.all()
    serializer_class = HighlightsSerializers
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadonly,)
    # lookup_field - using instance id.

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)


class JourneyListCreateViews(generics.ListCreateAPIView):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializers
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['username__name']
    # authentication_classes = (JWTAuthentication,)  # JWTAuthentication & SessionAuth are different...really.
    permission_classes = (IsAuthenticatedOrReadOnly,)
    
    def get_queryset(self):
        """
        filtering against queryset
        """
        queryset = Journey.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username__name=username)
        return queryset


class JourneyRUDViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializers
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadonly,)

    # lookup_field - using instance id.

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)