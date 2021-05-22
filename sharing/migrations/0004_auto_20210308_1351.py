# Generated by Django 3.1.7 on 2021-03-08 13:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sharing', '0003_sharingmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharingmessage',
            name='messagetext',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='sharingmessage',
            name='shareid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qnaid', to='sharing.sharing'),
        ),
        migrations.AddField(
            model_name='sharingmessage',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qna', to=settings.AUTH_USER_MODEL),
        ),
    ]
