from django.shortcuts import render,HttpResponse,redirect
from .models import service_provider_registrations,service
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from service.middleware.auth import login_req
from user .models import user_quries

def service_home(request):
    return render(request,'service_home.html')

def service_provider_register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        ser_name=request.POST.get('fname')
        ser_email=request.POST.get('email')
        ser_mobile=request.POST.get('mobile')
        pwd1=request.POST.get('pwd1')
        pwd2=request.POST.get('pwd2')
        ser_prov=service_provider_registrations.objects.create(username=username,ser_name=ser_name,ser_email=ser_email,ser_mobile=ser_mobile,ser_password=pwd1)
        ser_prov.save()   
    return render(request,'service_provider_register.html')

def service_provider_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if service_provider_registrations.objects.filter(username=username) and service_provider_registrations.objects.filter(ser_password=password):
            request.session['user_dt']=username
            user_dt=request.session.get('user_dt')
            return redirect('service_home')
        else:
             return redirect('service_provider_register')
    return render(request,'service_provider_login.html')

def servic_logout(request):
    logout(request)
    return redirect('service_provider_login')

@login_req
def add_services(request):
    ser=service()
    get_user=request.session.get('user_dt')
    if request.method=='POST':
        
        service_name=request.POST.get('servicename')
        service_descriptions=request.POST.get('servicedescriptions')
        service_cost=request.POST.get('servicecost')
        service_dt=service.objects.create(
            service_name=service_name,
            service_descriptions=service_descriptions,
            service_cost=service_cost,
            
    
        )
        service_provider_registrations.username=get_user
        service_dt.save()
    dt=service.objects.all()  

    return render(request,'add_services.html',{'dt':dt})

@login_req
def queries(request):
    get_user=request.session.get('user_dt')
    qur=user_quries.objects.filter(provider_name=get_user)
    qur1=user_quries.objects.filter(provider_name=get_user).count()
    print(qur1)
    print(request.user)
    return render(request,'ser_queries.html',{'qu':qur,'qu1':qur1})




# Create your views here.
