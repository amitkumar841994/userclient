from django.urls import path
from .import views
urlpatterns = [

path('',views.userhome,name='user_home'),
path('userregister',views.userregister,name='userregister'),
path('userlogin',views.userlogin,name='userlogin'),
path('userlogout',views.userlogout,name='userlogout'),
path('user_query/<int:pid>',views.user_query,name='user_query'),
path('user_service_details',views.user_service_details,name='user_service_details'),
path('user_query_status',views.user_query_status,name='user_status')
]