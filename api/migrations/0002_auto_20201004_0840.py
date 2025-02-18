# Generated by Django 3.1.2 on 2020-10-04 08:40

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterField(
            model_name='appointment',
            name='end_datetime',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2020, 10, 4, 8, 55, 32, 702384, tzinfo=utc))]),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='start_datetime',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2020, 10, 4, 8, 40, 32, 702205, tzinfo=utc))]),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=35, unique=True),
        ),
    ]
