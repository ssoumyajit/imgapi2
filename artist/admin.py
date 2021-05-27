from django.contrib import admin
from .models import Artist, ArtistData, Journey

# Register your models here.
admin.site.register(Artist)
admin.site.register(ArtistData)
admin.site.register(Journey)
