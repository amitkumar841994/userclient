# Generated by Django 4.1.3 on 2023-03-18 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0015_alter_service_provider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='provider',
        ),
    ]
