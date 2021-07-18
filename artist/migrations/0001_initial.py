# Generated by Django 3.1.7 on 2021-07-18 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wtitle', models.CharField(default='', max_length=255)),
                ('wflier', models.ImageField(default='', upload_to='works/')),
                ('wdate', models.DateField(blank=True, null=True)),
                ('wlocation', models.CharField(default='', max_length=255)),
                ('wupcoming', models.BooleanField(default=False)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joevent', models.CharField(default='', max_length=255)),
                ('jophoto1', models.ImageField(blank=True, default='', upload_to='events_attended/')),
                ('jophoto2', models.ImageField(default='', upload_to='events_attended/')),
                ('jophoto3', models.ImageField(default='', upload_to='events_attended/')),
                ('jophoto4', models.ImageField(default='', upload_to='events_attended/')),
                ('jophoto5', models.ImageField(default='', upload_to='events_attended/')),
                ('jodate', models.DateField(null=True)),
                ('jocontent', models.TextField(default='')),
                ('jolink', models.URLField(default='', max_length=255)),
                ('ishighlight', models.BooleanField(default=False)),
                ('isprivate', models.BooleanField(default=False)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ArtistData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(blank=True, default='', max_length=255)),
                ('quote', models.CharField(blank=True, default='', max_length=255)),
                ('introduction', models.TextField(blank=True, default='')),
                ('crew', models.CharField(blank=True, default='', max_length=255)),
                ('ig', models.CharField(blank=True, default='', max_length=200)),
                ('fb', models.CharField(blank=True, default='', max_length=200)),
                ('site', models.URLField(blank=True, default='')),
                ('gallery1', models.ImageField(blank=True, null=True, upload_to='gallery/')),
                ('gallery2', models.ImageField(blank=True, null=True, upload_to='gallery/')),
                ('gallery3', models.ImageField(blank=True, null=True, upload_to='gallery/')),
                ('gallery4', models.ImageField(blank=True, null=True, upload_to='gallery/')),
                ('vid1', models.URLField(blank=True, default='', max_length=255)),
                ('vid2', models.URLField(blank=True, default='', max_length=255)),
                ('vid3', models.URLField(blank=True, default='', max_length=255)),
                ('vid4', models.URLField(blank=True, default='', max_length=255)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='artistdata', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(null=True, upload_to='covers/')),
                ('thumb', models.ImageField(editable=False, upload_to='thumbnails/')),
                ('country', django_countries.fields.CountryField(default='', max_length=2)),
                ('artist_name', models.CharField(default='', max_length=255)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='artist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
