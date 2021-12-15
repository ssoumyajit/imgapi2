from django.contrib import admin
from .models import Artist, ArtistData, Journey, PhotoForJourney

# Register your models here.
admin.site.register(Artist)
admin.site.register(ArtistData)
admin.site.register(Journey)
admin.site.register(PhotoForJourney)
