# Generated by Django 4.1.3 on 2023-03-18 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0012_alter_service_provider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='provider',
            field=models.CharField(max_length=1000),
        ),
    ]