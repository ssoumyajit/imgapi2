# Generated by Django 3.1.7 on 2021-07-02 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0010_merge_20210626_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='cover',
            field=models.ImageField(default='', upload_to='covers/'),
        ),
    ]
