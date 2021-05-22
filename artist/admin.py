from django.contrib import admin
from .models import Artist, ArtistData, Highlights, Journey

# Register your models here.
admin.site.register(Artist)
admin.site.register(ArtistData)
admin.site.register(Highlights)
admin.site.register(Journey)
