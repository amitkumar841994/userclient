from django.db import models
class Food(models.Model):
    food_name=models.CharField(max_length=100,default='shdfgsjhd')
    food_price=models.FloatField(default=100)
    status=models.CharField(max_length=100,null=True,default='Pending')
    food_image=models.ImageField(upload_to='image/',null=True)


# Create your models here.
