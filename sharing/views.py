from django.shortcuts import render
from django.shortcuts import render
from .models import Sharing, Comments, LikesToSharing, SharingMessage
from rest_framework import viewsets
from .serializers import SharingSerializers, CommentSerializers, LikesToSharingSerializers, SharingMessageSerializers
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import filters
from rest_framework_simplejwt.authentication import JWTAuthentication


class SharingViewSets(viewsets.ModelViewSet):
    queryset = Sharing.objects.all()
    serializer_class = SharingSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['teacher__name', 'username__name']
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)


class LikesToSharingViewSets(viewsets.ModelViewSet):
    # here it does not make sense to list all the likes at one place,
    # rather make the queryset specific to an instance of sharing, same for comments also.
    queryset = LikesToSharing.objects.all()
    serializer_class = LikesToSharingSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['l_shareid__id']
    # authentication_classes = (JWTAuthentication,)
    # permission_classes = (IsAuthenticatedOrReadOnly,)


class CommentViewSets(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializers
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['c_shareid__id']

    def get_queryset(self):
        """
        filtering against queryset
        """
        queryset = Comments.objects.all()
        c_shareid = self.request.query_params.get('c_shareid', None)
        if c_shareid is not None:
            queryset = queryset.filter(c_shareid__id=c_shareid).order_by('-s_date')
        return queryset
    # authentication_classes = (JWTAuthentication,)
    # permission_classes = (IsAuthenticatedOrReadOnly,)

class SharingMessageViewSets(viewsets.ModelViewSet):
    queryset = SharingMessage.objects.all()
    serializer_class = SharingMessageSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['shareid__id']

    def get_queryset(self):
        """
        filtering against queryset
        """
        queryset = SharingMessage.objects.all()
        shareid = self.request.query_params.get('shareid', None)
        if shareid is not None:
            queryset = queryset.filter(shareid__id=shareid).order_by('-created')
        return queryset
