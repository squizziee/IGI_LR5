# Generated by Django 5.0.6 on 2024-09-09 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_companybanner'),
    ]

    operations = [
        migrations.AddField(
            model_name='companysponsor',
            name='website_link',
            field=models.CharField(default='/', max_length=100, verbose_name='Sponsor name'),
        ),
    ]
