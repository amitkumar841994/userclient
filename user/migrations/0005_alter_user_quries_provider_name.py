# Generated by Django 4.1.3 on 2022-12-17 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_quries_service_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_quries',
            name='provider_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
