from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SharingListCreateViews, SharingRUDViews, LikesForLearningView, LikesForLearningRUDView, \
    SharingMessageViewSets, LearningsCreateView, LearningsListView, LearningsRUDView, CommentsForLearningView, \
    CommentsForLearningRUDView, LoveForSharingView, LoveForSharingRUDView, CommentsForSharingView, \
    CommentsForSharingRUDView


router = DefaultRouter()
# qna
router.register('qna', SharingMessageViewSets)

app_name = 'sharing'

urlpatterns = [
    path(r'', include(router.urls)),
    path('sharing/', SharingListCreateViews.as_view()),
    path('sharing/<int:pk>', SharingRUDViews.as_view()),
    path('sharing/love/', LoveForSharingView.as_view()),
    path('sharing/love/<int:pk>', LoveForSharingRUDView.as_view()),
    path('sharing/comments/', CommentsForSharingView.as_view()),
    path('sharing/comments/<int:pk>', CommentsForSharingRUDView.as_view()),
    path('learnings/', LearningsCreateView.as_view()),
    path('learnings/list/', LearningsListView.as_view()),
    path('learnings/<int:pk>', LearningsRUDView.as_view()),
    path('learnings/likes/', LikesForLearningView.as_view()),
    path('learnings/likes/<int:pk>', LikesForLearningRUDView.as_view()),
    path('learnings/comments/', CommentsForLearningView.as_view()),
    path('learnings/comments/<int:pk>', CommentsForLearningRUDView.as_view()),
]
