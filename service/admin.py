from django.contrib import admin
from .models import service_provider_registrations,service

class serservice_provider_registrations_admin(admin.ModelAdmin):
    list_display=['id','username','ser_name','ser_email','ser_mobile']

admin.site.register(service_provider_registrations,serservice_provider_registrations_admin)

class service_admin(admin.ModelAdmin):
    list_display=['service_name','service_descriptions','service_cost','provider']



admin.site.register(service,service_admin)
# Register your models here.
