from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from service .models import service
from .models import user_quries,user_register
from django.contrib.auth.decorators import login_required
from user.middleware.auth import user_login_req


def userhome(request):
    return render(request,'index.html')

def userregister(request):
    user=User()
    if request.method=='POST':
          username=request.POST.get('username')
          pwd1=request.POST.get('pwd1')
          pwd2=request.POST.get('pwd2')
          fname=request.POST.get('fname')
          email=request.POST.get('email')
          mobile=request.POST.get('mobile')
          user=user_register.objects.create(username=username,email=email,password=pwd1,name=fname,mobile=mobile)
          user.save()
    return render(request,'user_register.html')

def userlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if user_register.objects.get(username=username) and user_register.objects.get(password=password):
            request.session['user_data']=username
            print(request.session.get('user_data'))
            return redirect('user_home')
    return render(request,'user_login.html')

def userlogout(request):
    logout(request)
    return redirect('userlogin')


def user_query(request,pid):
    srname=service.objects.all()
    dt=service.objects.get(id=pid)
    # print(dt.service_name)
    user_name=request.session.get('user_data')
    service_provider=str(dt.provider)
    if request.method=='POST':
        servicename=dt.service_name
        providername=service_provider
        username=user_name
        email=request.POST.get('emailid')
        query=request.POST.get('query')
        que=user_quries.objects.create(service_name=servicename,provider_name=providername,Useremail=email,queries=query,username=username)
        que.save()
    return render(request,'user_query.html',{'srname':srname,'pid':dt})

@user_login_req
def user_service_details(request):
    ser_det=service.objects.all()
    print(request.user)
    return render(request,'user_service_details.html',{'dt1':ser_det})

def user_query_status(request):
        user_name=request.session.get('user_data')
        qur_status=user_quries.objects.filter(username=user_name)
        return render(request,'user_query_status.html',{'status':qur_status})

# Create your views here.
