from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField

# --- for django-rest-passwordreset
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.core.mail import send_mail

from imgapiv1.constants import site_url, site_shortcut_name, site_full_name
# ---

GENDER_SELECTION = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('NS', 'Not Specified')
]


class User(AbstractUser):
    gender = models.CharField(max_length=20, choices=GENDER_SELECTION, default='NS')
    country = CountryField(default="")

# -----------------------------------------------------

'''
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "gebblesarts@gmail.com",
        # to:
        [reset_password_token.user.email]
    )
'''

class CustomPasswordResetView:

    @receiver(reset_password_token_created)
    def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
        """
        Handles password reset tokens
        When a token is created, an e-mail needs to be sent to the user
        :param sender: View Class that sent the signal
        :param instance: View Instance that sent the signal
        :param reset_password_token: Token Model Object
        :param args:
        :param kwargs:
        :return:
        """
        
        # send an email to the user
        context = {
            'current_user': reset_password_token.user,
            'username': reset_password_token.user.username,
            'email' : reset_password_token.user.email,
            'reset_password_url' : "{}/reset/{}".format("gebbles.art", reset_password_token.key),
            'site_name': site_shortcut_name,
            'site_domain': site_url
        }
    
        # render email text
        email_html_message = render_to_string('email/user_reset_password.html', context)
        email_plaintext_message = render_to_string('email/user_reset_password.txt', context)
    
        msg = EmailMultiAlternatives(
            # title:
            "password reset for {}".format(site_full_name),
            # message:
            email_plaintext_message,
            # from:
            "gebblesarts@gmail.com",
            # to:
            [reset_password_token.user.email]
    
        )
        msg.attach_alternative(email_plaintext_message, "text/html")
        msg.send()









'''
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
# from django_countries.fields import CountryField


# a manager to create user and superuser from user models
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates, validates and saves a new User"""
        if not email:
            raise ValueError('Users must have an email address')
        # above checks the validation for email address, user have to provide an email to enter
        user = self.model(email=self.normalize_email(email),
                          **extra_fields)  # normalize_email helps to check if all the gmail.com in lowe case
        user.set_password(password)  # set_password helps to encrypt the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ Custom User model that supports using email instead of username -- /
                                           supported by PermissionsMixins """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # country = CountryField(default = "IN")

    objects = UserManager()  # creates a new user manager for our object
    USERNAME_FIELD = 'email'
'''
