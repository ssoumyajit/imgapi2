from rest_framework import serializers
from .models import Artist, ArtistData, Journey, Work
from .models import STYLES_CHOICES
from user.models import User
from django_countries.serializers import CountryFieldMixin


# from portfolio import settings


class ArtistSerializers(CountryFieldMixin, serializers.ModelSerializer):
    # overridden username here
    # this is where the bug is, so don can patch on Batala while updating in postman
    # username = serializers.ReadOnlyField(source='username.name')
    # username = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # HiddenField https://stackoverflow.com/questions/49557741/django-hiddenfield-value-generated-on-views
    username = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Artist
        fields = ['username', 'artist_name', 'cover', 'thumb', 'country']
        # extra_kwargs = {
        # 'url': {'lookup_field': 'owner'}
        # }

    '''
    def __init__(self, *args, **kwargs):

        # don't return covers when listing artists
        if kwargs['context']['view'].action == 'list':
            del self.fields['cover']

        super().__init__(*args, **kwargs)
    '''


class ArtistDataSerializers(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
    styles = serializers.MultipleChoiceField(choices=STYLES_CHOICES, allow_blank=True)
    # source='get_styles_display'

    class Meta:
        model = ArtistData
        fields = ['username', 'style', 'quote', 'introduction', 'crew', 'ig', 'fb', 'site', 'gallery1', 'gallery2',
                  'gallery2', 'gallery3', 'gallery4', 'styles', 'vid1', 'vid2', 'vid3', 'vid4']


class JourneySerializers(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Journey
        fields = "__all__"


class JourneyListSerializers(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Journey
        fields = ['id', 'username', 'jodate', 'jophoto1', 'isprivate', 'ishighlight']
        read_only_fields = ['id', 'username', 'jodate', 'jophoto1', 'isprivate', 'ishighlight']


class WorkSerializers(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Work
        fields = "__all__"
# ------------------------------------------------------------
