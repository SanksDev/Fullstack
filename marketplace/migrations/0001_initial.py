# Generated by Django 3.2.8 on 2023-04-01 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50)),
                ('descrip', models.CharField(max_length=400)),
            ],
        ),
    ]
