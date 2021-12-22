# Generated by Django 3.2.6 on 2021-10-15 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20211015_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conteudo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_conteudo', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='oa',
            name='conteudo',
        ),
        migrations.AddField(
            model_name='oa',
            name='conteudo',
            field=models.ManyToManyField(to='app.Conteudo'),
        ),
    ]
