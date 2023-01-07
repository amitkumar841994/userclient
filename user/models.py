from django.db import models

class user_quries(models.Model):
    service_name=models.CharField(max_length=200)
    provider_name=models.CharField(max_length=100)
    Useremail=models.CharField(max_length=100)
    queries=models.CharField(max_length=700)

class user_register(models.Model):
    name=models.CharField(max_length=60)
    username=models.CharField(max_length=70)
    email=models.CharField(max_length=70)
    mobile=models.IntegerField()
    password=models.CharField(max_length=100)



# Create your models here.
