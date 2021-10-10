# Generated by Django 3.1.7 on 2021-10-10 01:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sharing', '0007_auto_20211008_0523'),
        ('gebblesalert', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='e1t1notification',
            name='notification_type',
            field=models.IntegerField(choices=[(1, 'Love'), (2, 'Comment'), (3, 'e1t1_creation')], default=3),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='LearningsRelatedNotifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('notification_type', models.IntegerField(choices=[(1, 'Like'), (2, 'Comment'), (3, 'learning_creation')])),
                ('is_seen', models.BooleanField(default=False)),
                ('learningobject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notilearningobj', to='sharing.learnings')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notitouser_learning_like_comment', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifromuser_learning_like_comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
