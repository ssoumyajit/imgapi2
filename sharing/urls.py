from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SharingListCreateViews, SharingRUDViews, CommentViewSets, LikesToSharingViewSets, SharingMessageViewSets

router = DefaultRouter()

# sharing
# router.register('sharing', SharingListCreateViews)
# likesToSharing
router.register('likes', LikesToSharingViewSets)
# comments
router.register('comments', CommentViewSets)
# qna
router.register('qna', SharingMessageViewSets)

app_name = 'sharing'

urlpatterns = [
    path(r'', include(router.urls)),
    path('sharing/', SharingListCreateViews.as_view()),
    path('sharing/<int:pk>', SharingRUDViews.as_view())
]
