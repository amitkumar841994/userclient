from django.shortcuts import render,redirect
from .models import Food
from django.core.files.storage import FileSystemStorage
from .form import *

def user_food(request):
    f_data=Food.objects.all()
    form=''
    if request.method=='POST':
        form=foodform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    return render(request,'Food.html',{'f':f_data,'form':form})

def food_order(request,pid):
    ord_id=Food.objects.get(id=pid)
    ordr_up=Food.objects.filter(pk=pid).update(status='Placed')
    return redirect(user_food)

def cal_order(request,pid):
    ord_id=Food.objects.get(id=pid)
    ordr_up=Food.objects.filter(pk=pid).update(status='Canceled')
    return redirect(user_food)

def order(request):
    var='Placed'
    pl=Food.objects.filter(status=var)

    return render(request,'chef_order.html',{'pl':pl})

# Create your views here.
