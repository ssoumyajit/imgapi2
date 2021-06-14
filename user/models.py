from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
from django_countries.fields import CountryField


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

    cover = models.ImageField(default="", upload_to="covers/", blank=True)
    country = CountryField(default="", blank=True)
    artist_name = models.CharField(max_length=255, default="", blank=True) 

    objects = UserManager()  # creates a new user manager for our object
    USERNAME_FIELD = 'email'
