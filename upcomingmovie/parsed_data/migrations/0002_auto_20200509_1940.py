# Generated by Django 3.0.3 on 2020-05-09 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parsed_movie',
            name='date',
            field=models.CharField(max_length=256),
        ),
    ]
