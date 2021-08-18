# from django.shortcuts import render
from .models import Artist, ArtistData, Journey, Work
from .serializers import ArtistSerializers, ArtistDataSerializers, JourneySerializers, JourneyListSerializers, \
    WorkSerializers, ArtistListSerializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from permissions import IsOwnerOrReadonly
from rest_framework import generics
# from rest_framework.parsers import FormParser, MultiPartParser
from django.db.models import Q
# from rest_framework.decorators import api_view
# from rest_framework.response import Response


class ArtistCreateViews(generics.CreateAPIView):
    serializer_class = ArtistSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ArtistListViews(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistListSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        """
        filtering against queryset
        """
        queryset = Artist.objects.all()
        query = self.request.query_params.get('query', None)

        if query is not None:
            queryset = queryset.filter(Q(username__username__icontains=query) | Q(artist_name__icontains=query))
            return queryset

        return queryset
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
    lookup_field = "username__username"
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
    lookup_field = 'username__username'
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadonly,)

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)


'''
# search an artist functionality
@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        artists = Artist.objects.filter(Q(username__icontains=query) | Q(artist_name__icontains=query))
        serializer = ArtistSerializers(artists, many=True)
        return Response(serializer.data)
    else:
        return Response({"artists": []})
'''


class JourneyCreateViews(generics.CreateAPIView):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializers
    permission_classes = (IsAuthenticated,)


class JourneyListViews(generics.ListAPIView):
    queryset = Journey.objects.all()
    serializer_class = JourneyListSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # feature for keeping a post private/public.
    def get_queryset(self):
        """
        filtering against queryset
        """
        queryset = Journey.objects.all()
        username = self.request.query_params.get('username', None)

        if username is not None:

            # logic to filter based on normal user or loggedIn user
            if self.request.user.is_authenticated and username == self.request.user.username:
                queryset = queryset.filter(username__username=username)
                return queryset
            else:
                queryset = queryset.filter(username__username=username)
                queryset = queryset.filter(isprivate=False)
                return queryset
        return queryset


class JourneyRUDViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializers
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadonly,)

    # lookup_field - using instance id.

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)

    # def perform_update ??


class WorkListCreateViews(generics.ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        """
        filtering against queryset
        """
        queryset = Work.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username__username=username)
        return queryset


class WorkRUDViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializers
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadonly,)

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)
