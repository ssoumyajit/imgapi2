# Generated by Django 3.1.7 on 2021-10-08 05:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sharing', '0005_likesforlearning'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentsForLearning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('learningid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cflid', to='sharing.learnings')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cfluser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentsForSharing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField(default='')),
                ('shareid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cfsid', to='sharing.sharing')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cfsuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LoveForSharing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('shareid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lfsid', to='sharing.sharing')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lfsuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='likestosharing',
            name='l_liker',
        ),
        migrations.RemoveField(
            model_name='likestosharing',
            name='l_shareid',
        ),
        migrations.AddField(
            model_name='likesforlearning',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 10, 8, 5, 5, 3, 444323, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.DeleteModel(
            name='LikesToSharing',
        ),
    ]