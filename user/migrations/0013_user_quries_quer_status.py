# Generated by Django 4.1.3 on 2023-03-21 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_user_quries_createdate_user_quries_resloved_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_quries',
            name='quer_status',
            field=models.CharField(default='Pending', max_length=1000),
        ),
    ]
