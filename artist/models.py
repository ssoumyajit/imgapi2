from django.db import models
from multiselectfield import MultiSelectField
from django.conf import settings
from django_countries.fields import CountryField
import time
import uuid

# for testing artist creation when the user is created using signals.
# from django.core.signals import request_finished
from django.dispatch import receiver
from django.db.models.signals import post_save
from user.models import User

# for image manipulations
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO
import os.path
from imgapiv1.settings import COVER_THUMBNAIL_SIZE

STYLES_CHOICES = ((1, 'HIPHOP'),
                 (2, 'HOUSE'),
                 (3, 'POPPING'),
                 (4, 'LOCKING'),
                 (5, 'BREAKING'),
                 (6, 'EXPERIMENTAL'),
                 (7, 'OTHER'),
                 (8, 'STILL EXPLORING'))


def scramble_uploaded_filename(file):

    now = str(int(time.time()))
    filepath = 'gallery/'
    extension = file.split(".")[-1]
    return "{}+{}.{}".format(filepath, uuid.uuid4(), extension)


class Artist(models.Model):
    username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="artist", blank=False)
    cover = models.ImageField(default="", upload_to="covers/", blank=True)
    thumb = models.ImageField(upload_to="thumbnails/", blank=True, editable=False)
    country = CountryField(default="", blank=True)
    artist_name = models.CharField(max_length=255, default="", blank=True)

    def save(self, *args, **kwargs):
        if not self.make_thumbnail():
            # try except else n then raise exception
            # raise Exception('could not create thumbnail, is the FileType valid ?')
            pass
        super(Artist, self).save(*args, **kwargs)

    def make_thumbnail(self):
        if self.cover:

            image = Image.open(self.cover)
            image.thumbnail(COVER_THUMBNAIL_SIZE, Image.ANTIALIAS)
            thumbnail_name, thumbnail_extension = os.path.splitext(self.cover.name)
            thumbnail_extension = thumbnail_extension.lower()
            thumbnail_filename = thumbnail_name + "_thumb" + thumbnail_extension

            if thumbnail_extension in ['.jpg', '.jpeg']:
                filetype = 'JPEG'
            elif thumbnail_extension == '.png':
                filetype = 'PNG'
            else:
                return False

            # save the thumbnail in memory file as StringIO
            temp_thumbnail = BytesIO()
            image.save(temp_thumbnail, filetype)
            temp_thumbnail.seek(0)

            # Load a ContentFile into the thumbnail field so it gets saved.
            # set save=False, otherwise it will run in an infinite loop
            self.thumb.save(thumbnail_filename, ContentFile(temp_thumbnail.read()), save=False)
            temp_thumbnail.close()
            return True
            # https://stackoverflow.com/questions/23922289/django-pil-save-thumbnail-version-right-when-image-is-uploaded


class ArtistData(models.Model):
    username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="artistdata")
    style = models.CharField(max_length=15, default="", blank=True)
    styles = MultiSelectField(choices=STYLES_CHOICES, default='')
    quote = models.CharField(max_length=255, default="", blank=True)
    introduction = models.TextField(default="", blank=True)
    crew = models.CharField(max_length=255, default="", blank=True)
    ig = models.CharField(max_length=200, default="", blank=True)
    fb = models.CharField(max_length=200, default="", blank=True)
    site = models.URLField(max_length=200, default="", blank=True)
    gallery1 = models.ImageField(null=True, blank=True, upload_to='gallery/')
    gallery2 = models.ImageField(null=True, blank=True, upload_to='gallery/')
    gallery3 = models.ImageField(null=True, blank=True, upload_to='gallery/')
    gallery4 = models.ImageField(null=True, blank=True, upload_to='gallery/')
    vid1 = models.URLField(max_length=255, default="", blank=True)
    vid2 = models.URLField(max_length=255, default="", blank=True)
    vid3 = models.URLField(max_length=255, default="", blank=True)
    vid4 = models.URLField(max_length=255, default="", blank=True)

    """
        def save(self, *args, **kwargs):
        super(ArtistData, self).save(*args, **kwargs)
        gallery1 = Image.open(self.gallery1.path)
        gallery1.thumbnail((240, 240), Image.ANTIALIAS)
        gallery1.save(self.gallery1.path, optimize=True, quality=90)
    """


@receiver(post_save, sender=User)
def create_artist_artistdata(sender, instance, created, **kwargs):
    if created:
        Artist.objects.create(username=instance)
        ArtistData.objects.create(username=instance)

# https://stackoverflow.com/questions/33659994/django-rest-framework-create-user-and-user-profile


class Journey(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # must
    joevent = models.CharField(max_length=255, default="", blank=False)  # must
    jophoto = models.ImageField(default="", upload_to="events_attended/", blank=False)  # must
    jodate = models.DateField(null=True, blank=True)
    jocontent = models.TextField(default="", blank=True)
    jolink = models.URLField(max_length=255, default="", blank=True)
    ishighlight = models.BooleanField(default=False)
    isprivate = models.BooleanField(default=False)

    def save(self, *args, ** kwargs):
        super(Journey, self).save(*args, **kwargs)
        photo = Image.open(self.jophoto.path)
        photo.thumbnail((240, 180), Image.ANTIALIAS)
        photo.save(self.jophoto.path, optimize=True, quality=90)

    def __str__(self):
        return self.jodate


class Work(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    wtitle = models.CharField(max_length=255, default="", blank=False)
    wflier = models.ImageField(default="", upload_to="works/", blank=False)
    wdate = models.DateField(null=True, blank=True)
    wlocation = models.CharField(max_length=255, default="", blank=False)
    wupcoming = models.BooleanField(default=False)
    test = models.CharField(max_length=25, null=True)

    def save(self, *args, ** kwargs):
        super(Work, self).save(*args, **kwargs)
        wflier = Image.open(self.wflier.path)
        wflier.thumbnail((240, 180), Image.ANTIALIAS)
        wflier.save(self.wflier.path, optimize=True, quality=90)

    def __str__(self):
        return self.wdate

# null = True means, when u do not put anything in the field , it will be set NULL in the database
# blank = True/False   related only to the forms
# default = None, default=None does not allow or disallow a None value to be used. It simply tells #
# Django what should be the value of the field if it is not specified. null=True does allow None
# to be used in the Python code. It is treated as NULL in the database. And you're right about blank being used for form validation.

# gallery limit:
# https://stackoverflow.com/questions/31846152/limit-number-of-foreign-keys-based-on-how-many-foreign-keys-refer-to-that-model
