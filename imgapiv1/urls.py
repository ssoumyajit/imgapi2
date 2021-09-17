"""imgapiv1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView
from dj_rest_auth.views import PasswordResetConfirmView, PasswordResetView
from user.views import ApiPasswordResetView


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    # path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('dj_rest_auth.urls')),
    path('api/v1/auth/registration/account-confirm-email/<str:key>/', ConfirmEmailView.as_view(),),
    # path('api/v1/auth/registration/resend-email/'),
    path('api/v1/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/v1/auth/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),

    # this path is used to generate email content for password reset request
    # from dj-rest-auth API; format is same as used by default django auth so
    # the generated URL must be translated to be used with allauth

    path('api/v1/auth/password/reset/confirm/<uidb64>/<token>/',
          ApiPasswordResetView.as_view(),
          name='password_reset_confirm'),
    path('api/v1/accounts/', include('allauth.urls')),

    # path('api/v1/auth/password/reset/confirm/<slug:uidb64>/<slug:token>/',
    # PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('api/v1/auth/password/reset/', PasswordResetView.as_view()),
    # path('api/v1/user/', include('user.urls')),
    path('api/v1/artist/', include('artist.urls')),
    path('api/v1/e1t1/', include('sharing.urls')),
    path('api/v1/inquiry/', include('inquiry.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
