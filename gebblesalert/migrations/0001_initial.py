# Generated by Django 3.1.7 on 2021-09-18 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sharing', '0002_auto_20210908_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='E1T1Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('is_seen', models.BooleanField(default=False)),
                ('e1t1object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notie1t1obj', to='sharing.sharing')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notitouser', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifromuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]