from django.urls import path
from .import views
urlpatterns = [
    path('service_provider_register',views.service_provider_register,name='service_provider_register'),
    path('service_provider_login',views.service_provider_login,name='service_provider_login'),
    path('service_home',views.service_home,name='service_home'),
    path('add_services',views.add_services,name='add_services'),
    path('queries',views.queries,name='queries'),
    path('servic_logout',views.servic_logout,name='servic_logout'),

]