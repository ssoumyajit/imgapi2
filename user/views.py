from allauth.account.forms import \
    default_token_generator as allauth_token_generator
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str
from django.utils.http import int_to_base36, urlsafe_base64_decode
# from django.contrib.auth.models import User
from django.views import View
from .models import User
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy


class ApiPasswordResetView(View):
    """ Wrapper to change the uid encoding and token
    used by dj_rest_auth to the method used by allauth
    """

    def get(self, *args, **kwargs):
        uidb36 = None
        token = kwargs.get('token')
        try:
            uid = force_str(urlsafe_base64_decode(kwargs.get('uidb64')))
            user = User.objects.get(pk=uid)
            uidb36 = int_to_base36(int(uid))
            # validate default token
            if default_token_generator.check_token(user, token):
                # generate allauth token
                token = allauth_token_generator.make_token(user)
            else:
                token = None
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Http404()
        # redirect to Allauth password reset link
        return HttpResponseRedirect(
            reverse_lazy('account_reset_password_from_key', args=[uidb36, token])
        )

# https://www.rootstrap.com/blog/how-to-change-the-rest-auth-reset-password-email-to-a-custom-html-template/
# above article helped with dj_rest_auth password reset email templates.
# also allauth docs is very helpful. DO check for the project level variables that u can use
# u need some of them like resend email confirmation, deactivate it after 3 days etc.




"""
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from .serializers import UserSerializer, CustomTokenSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.settings import api_settings

from rest_framework import generics, authentication, permissions


class CreateUserView(CreateAPIView):
    # create a new user in the system
    serializer_class = UserSerializer


class CustomObtainAuthToken(TokenObtainPairView):
    serializer_class = CustomTokenSerializer


    # def post(self, request, *args, **kwargs):
        # response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        # token = Token.objects.get(key=response.data['token'])
        # return Response({'token': token.key, 'id': token.user_id})
        # return Response({'token': token.key, 'id': token.user_id, 'user': token.user_email})


class ManageUserView(RetrieveUpdateAPIView):

    # manage the authenticated user.

    serializer_class = UserSerializer  # CustomTokenSerializer   change later.
    authentication_class = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user


# https://github.com/encode/django-rest-framework/issues/2414      getting back user data alogn with token
# https://stackoverflow.com/questions/53480770/how-to-return-custom-data-with-access-and-refresh-tokens-to-identify-users-in-dj/53512800

# simple jwt
# https://stackoverflow.com/questions/53480770/how-to-return-custom-data-with-access-and-refresh-tokens-to-identify-users-in-dj/53512800

"""

'''
#class CreateTokenView(ObtainAuthToken):
class CreateTokenView(TokenObtainPairView):
    
    # create a new auth token for the user.
    
    #serializer_class = AuthTokenSerializer
    serializer_class = CustomTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
'''

