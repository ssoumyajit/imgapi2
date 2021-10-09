from django.shortcuts import render
from .models import Sharing, SharingMessage, Learnings, LikesForLearning, CommentsForLearning, LoveForSharing, \
    CommentsForSharing
from rest_framework import viewsets
from .serializers import SharingSerializers, SharingMessageSerializers, LearningsSerializers, \
    LearningsSerializersWithoutVideo, LikesForLearningSerializer, CommentsForLearningSerializer, \
    LoveForSharingSerializer, CommentsForSharingSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import filters
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from django.db.models import Q
from permissions import IsOwnerOrReadonly


class SharingListCreateViews(generics.ListCreateAPIView):
    queryset = Sharing.objects.all()
    serializer_class = SharingSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        """
        filtering against queryset
        """
        queryset = Sharing.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(Q(username__username=username) | Q(teacher__username=username))
        return queryset


class SharingRUDViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sharing.objects.all()
    serializer_class = SharingSerializers
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadonly)

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)


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


class LearningsCreateView(generics.CreateAPIView):
    serializer_class = LearningsSerializers
    permission_classes = (IsAuthenticated, )


class LearningsListView(generics.ListAPIView):
    serializer_class = LearningsSerializersWithoutVideo
    queryset = Learnings.objects.all()

    # need a pagination function here
    # need to write an algorithm to select and shuffle content here.

    def get_queryset(self):
        queryset = Learnings.objects.all()
        shareidobj = self.request.query_params.get('shareidobj', None)
        if shareidobj is not None:
            # queryset = queryset.filter(Q(shareidobj=shareidobj))  # ???????? is Q the reason for url redundancy
            queryset = queryset.filter(shareidobj__id=shareidobj).order_by('-timestamp')
        return queryset


class LearningsRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LearningsSerializers
    queryset = Learnings.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadonly, )


class LikesForLearningView(generics.ListCreateAPIView):
    serializer_class = LikesForLearningSerializer
    queryset = LikesForLearning.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        queryset = LikesForLearning.objects.all()
        learningidobj = self.request.query_params.get('learningidobj', None)
        if learningidobj is not None:
            queryset = queryset.filter(learningidobj__id=learningidobj).order_by('-timestamp')
        return queryset


class LikesForLearningRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LikesForLearningSerializer
    queryset = LikesForLearning.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadonly,)


class CommentsForLearningView(generics.ListCreateAPIView):
    serializer_class = CommentsForLearningSerializer
    queryset = CommentsForLearning.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        queryset = CommentsForLearning.objects.all()
        learningidobj = self.request.query_params.get('learningidobj', None)
        if learningidobj is not None:
            queryset = queryset.filter(learningidobj__id=learningidobj).order_by('-timestamp')
        return queryset


class CommentsForLearningRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentsForLearningSerializer
    queryset = CommentsForLearning.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadonly,)


class LoveForSharingView(generics.ListCreateAPIView):
    serializer_class = LoveForSharingSerializer
    queryset = LoveForSharing.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        queryset = LoveForSharing.objects.all()
        shareidobj = self.request.query_params.get('shareidobj', None)
        if shareidobj is not None:
            queryset = queryset.filter(shareidobj__id=shareidobj).order_by('-timestamp')
        return queryset


class LoveForSharingRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LoveForSharingSerializer
    queryset = LoveForSharing.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadonly,)


class CommentsForSharingView(generics.ListCreateAPIView):
    serializer_class = CommentsForSharingSerializer
    queryset = CommentsForSharing.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        queryset = CommentsForSharing.objects.all()
        shareidobj = self.request.query_params.get('shareidobj', None)
        if shareidobj is not None:
            queryset = queryset.filter(shareidobj__id=shareidobj).order_by('-timestamp')
        return queryset


class CommentsForSharingRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentsForSharingSerializer
    queryset = CommentsForSharing.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadonly,)








"""
'''
class SharingViewSets(viewsets.ModelViewSet):
    queryset = Sharing.objects.all()
    serializer_class = SharingSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['teacher__name', 'username__name']
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
'''

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
        
        queryset = Comments.objects.all()
        c_shareid = self.request.query_params.get('c_shareid', None)
        if c_shareid is not None:
            queryset = queryset.filter(c_shareid__id=c_shareid).order_by('-s_date')
        return queryset
    # authentication_classes = (JWTAuthentication,)
    # permission_classes = (IsAuthenticatedOrReadOnly,)
"""
