from django.db import models


class service_provider_registrations(models.Model):
    username=models.CharField(max_length=50)
    ser_name=models.CharField(max_length=50)
    ser_email=models.CharField(max_length=30)
    ser_mobile=models.IntegerField()
    ser_password=models.CharField(max_length=50)
    def __str__(self):
        return self.username

class service(models.Model):
    service_name=models.CharField(max_length=50)
    service_descriptions=models.CharField(max_length=1000)
    service_cost=models.FloatField()
    provider=models.CharField(max_length=1000)


# Create your models here.
