# Generated by Django 3.2.6 on 2021-08-19 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=2048)),
                ('link', models.CharField(max_length=2048)),
                ('tag', models.CharField(max_length=50)),
                ('conteudo', models.CharField(max_length=255)),
                ('inserir', models.CharField(max_length=255)),
            ],
        ),
    ]
