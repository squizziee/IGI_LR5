# Generated by Django 5.0.6 on 2024-05-15 08:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0002_alter_order_deadline_date_alter_order_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deadline_date',
            field=models.DateField(default=datetime.datetime(2024, 5, 14, 11, 35, 21, 771117), verbose_name='Deadline of order completion'),
        ),
    ]
