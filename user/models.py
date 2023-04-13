from django.db import models
from datetime import datetime

class user_quries(models.Model):
    service_name=models.CharField(max_length=200)
    provider_name=models.CharField(max_length=100)
    Useremail=models.CharField(max_length=100)
    username=models.CharField(max_length=100,null=True)
    queries=models.CharField(max_length=700)
    quer_status=models.CharField(max_length=1000, default='Pending')
    createdate=models.DateTimeField(default=datetime.now,null=True)
    resloved_date=models.DateTimeField(null=True)

class user_register(models.Model):
    name=models.CharField(max_length=60)
    username=models.CharField(max_length=70)
    email=models.CharField(max_length=70)
    mobile=models.IntegerField()
    password=models.CharField(max_length=100)



# Create your models here.
