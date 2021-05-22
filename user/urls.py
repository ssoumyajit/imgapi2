from django.urls import path
from rest_framework import generics
from .views import CreateUserView, ManageUserView, CustomObtainAuthToken
from rest_framework_simplejwt import views as jwt_views

app_name = 'user'
# for using django reverse() function, it is a django utility function
# https://docs.djangoproject.com/en/3.0/ref/urlresolvers/

urlpatterns = [
    path('token/', CustomObtainAuthToken.as_view(), name='token_obtain_pair'),
    path('create/', CreateUserView.as_view(), name='create'),
    path('update/', ManageUserView.as_view(), name='update'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]