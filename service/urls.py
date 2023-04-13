from django.urls import path
from .import views
urlpatterns = [
    path('service_provider_register',views.service_provider_register,name='service_provider_register'),
    path('service_provider_login',views.service_provider_login,name='service_provider_login'),
    path('service_home',views.service_home,name='service_home'),
    path('add_services',views.add_services,name='add_services'),
    path('delete_services\<int:pid>',views.delete_sevices,name='delete_sevices'),
    path('update_service\<int:pid>',views.update_service,name='update_service'),
    path('queries',views.queries,name='queries'),
    path('queries_status\<int:pid>',views.queries_status,name='queries_status'),
    path('servic_logout',views.servic_logout,name='servic_logout')

]