# Generated by Django 4.1.3 on 2022-12-31 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_rename_username_service_provider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='provider',
        ),
        migrations.AddField(
            model_name='service',
            name='provider',
            field=models.ManyToManyField(blank=True, to='service.service_provider_registrations', verbose_name='provider'),
        ),
    ]
