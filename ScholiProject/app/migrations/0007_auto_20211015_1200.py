# Generated by Django 3.2.6 on 2021-10-15 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oa',
            old_name='tag',
            new_name='tags',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='nometag',
            new_name='nametag',
        ),
    ]