# Generated by Django 3.1.7 on 2021-07-09 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0018_auto_20210708_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistdata',
            name='style',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]