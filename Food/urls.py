from django.urls import path
from .import views

urlpatterns=[
    path('user_food',views.user_food,name='user_food'),
    path('food_order/<int:pid>',views.food_order,name='food_order'),
    path('cal_order/<int:pid>',views.cal_order,name='cal_order'),
    path('order',views.order,name='order')

]