# Generated by Django 3.2.6 on 2021-12-18 15:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0015_oa_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='oa',
            name='favoritos',
            field=models.ManyToManyField(blank=True, default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
