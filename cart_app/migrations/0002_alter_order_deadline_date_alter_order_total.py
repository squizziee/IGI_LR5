# Generated by Django 5.0.6 on 2024-05-15 08:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deadline_date',
            field=models.DateField(default=datetime.datetime(2024, 5, 14, 11, 33, 48, 480283), verbose_name='Deadline of order completion'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.FloatField(default=0, verbose_name='Total price with all additions'),
        ),
    ]
