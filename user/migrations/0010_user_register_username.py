# Generated by Django 4.1.3 on 2022-12-21 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_user_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_register',
            name='username',
            field=models.CharField(default=1, max_length=70),
            preserve_default=False,
        ),
    ]
