# Generated by Django 3.1.7 on 2021-09-07 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alert',
            old_name='student',
            new_name='username',
        ),
    ]
