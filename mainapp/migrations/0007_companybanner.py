# Generated by Django 5.0.6 on 2024-09-09 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_companysponsor_companyinfo_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='Banner image')),
                ('description', models.TextField(verbose_name='Banner info')),
            ],
        ),
    ]