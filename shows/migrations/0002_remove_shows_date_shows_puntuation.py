# Generated by Django 4.1.2 on 2023-04-13 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shows',
            name='date',
        ),
        migrations.AddField(
            model_name='shows',
            name='puntuation',
            field=models.IntegerField(default=5),
        ),
    ]
