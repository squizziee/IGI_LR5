# Generated by Django 5.0.6 on 2024-05-16 12:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_companyinfo'),
        ('service_app', '0004_alter_master_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.IntegerField(default=15, verbose_name='Discount in percent')),
                ('is_active', models.BooleanField(default=True, verbose_name='Can be used?')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_app.service')),
            ],
        ),
    ]
