# Generated by Django 5.0.6 on 2024-10-23 19:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0029_alter_order_deadline_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deadline_date',
            field=models.DateField(default=datetime.datetime(2024, 10, 22, 22, 32, 20, 612855), verbose_name='Deadline of order completion'),
        ),
    ]
