# Generated by Django 4.1.3 on 2022-12-10 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_rename_provider_service_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='username',
            new_name='provider',
        ),
    ]