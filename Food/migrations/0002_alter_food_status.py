# Generated by Django 4.1.3 on 2023-03-23 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
