# Generated by Django 3.1.7 on 2021-09-27 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sharing', '0002_auto_20210908_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Learnings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('video', models.FileField(default='', upload_to='sharing/videos/')),
                ('shareidobj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='learningid', to='sharing.sharing')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='learninguser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]