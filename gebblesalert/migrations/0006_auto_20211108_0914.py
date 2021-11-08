# Generated by Django 3.1.7 on 2021-11-08 09:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gebblesalert', '0005_notificationse1t1_receiver2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationse1t1',
            name='receiver2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notitouser2object', to=settings.AUTH_USER_MODEL),
        ),
    ]