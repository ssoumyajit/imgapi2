# Generated by Django 3.1.7 on 2021-05-22 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artist', '0003_journey_ishighlight'),
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
    ]
