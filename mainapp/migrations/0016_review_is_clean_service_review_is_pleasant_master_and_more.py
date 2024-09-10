# Generated by Django 5.0.6 on 2024-09-10 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='is_clean_service',
            field=models.BooleanField(default=False, verbose_name='Was the job done clean'),
        ),
        migrations.AddField(
            model_name='review',
            name='is_pleasant_master',
            field=models.BooleanField(default=False, verbose_name='Was master pleasant to communicate with'),
        ),
        migrations.AddField(
            model_name='review',
            name='speed_rating',
            field=models.IntegerField(default=4, verbose_name='Service speed rating from 1 to 5'),
        ),
    ]
