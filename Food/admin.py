from django.contrib import admin
from .models import Food


class Food_admin(admin.ModelAdmin):
    list_display=['food_name','food_price','status','food_image']
admin.site.register(Food,Food_admin)

# Register your models here.
