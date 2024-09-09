# Generated by Django 5.0.6 on 2024-09-07 17:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0009_alter_order_deadline_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deadline_date',
            field=models.DateField(default=datetime.datetime(2024, 9, 6, 20, 49, 19, 239460), verbose_name='Deadline of order completion'),
        ),
    ]
