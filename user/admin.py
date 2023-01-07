from django.contrib import admin
from .models import user_quries,user_register

class user_quries_admin(admin.ModelAdmin):
    list_display=['service_name','provider_name','Useremail','queries']

admin.site.register(user_quries,user_quries_admin)

class user_register_admin(admin.ModelAdmin):
    list_display=['name','email','mobile','password','username']
admin.site.register(user_register,user_register_admin)

# Register your models here.
