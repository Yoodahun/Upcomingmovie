# Generated by Django 3.0.3 on 2020-05-09 10:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20200509_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_movie',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 5, 9, 19, 40, 5, 303550)),
        ),
    ]
