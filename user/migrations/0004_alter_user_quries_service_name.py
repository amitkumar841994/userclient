# Generated by Django 4.1.3 on 2022-12-17 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_user_quries_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_quries',
            name='service_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
