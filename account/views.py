from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from account.models import member,membership,start_end_time
from datetime import datetime
from django.utils import timezone
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'home.html')


# def login(request):
#     if member.objects.filter(real_name=request.POST['real_name']).exists():
#         obj = member.objects.get(real_name=request.POST['real_name'])
#         id = obj.id
#         real_name = obj.real_name
#         tz = obj.tz
#         print(obj.last_login)
#         last_login = timezone.now()
#         last_logout = timezone.now()
#         obj.delete()
#         update_obj = member.objects.create(id=id,real_name=real_name,tz=tz,last_login=last_login,last_logout=last_logout)
#         update_obj.save()
#         return render(request, 'login.html')
#     else:
#         return redirect('/')

def login(request):
    if request.method == 'POST':
        if membership.objects.filter(real_name=request.POST['real_name']).exists():
            obj = membership.objects.get(real_name=request.POST['real_name'])
            data = {}
            data['ID'] = obj.id
            data['REAL_NAME'] = obj.real_name
            data['TZ'] = obj.tz
            data['START TIME'] = obj.activity_period.start_time
            data['END TIME'] = obj.activity_period.end_time

            obj.delete()
            s1 = start_end_time(start_time=timezone.now(),end_time=timezone.now())
            s1.save()
            update_obj = membership.objects.create(id=data['ID'],real_name=data['REAL_NAME'],tz=data['TZ'], activity_period=s1)
            update_obj.save()
            return render(request,'login.html',{'data':data})
        else:
            messages.error(request,'real name not existed')
            return redirect("/")
    else:
        return redirect("/")

def register(request):
    if request.method == 'POST':
        id = request.POST.get('unique_id')
        real_name = request.POST.get('real_name')
        tz = request.POST.get('tz')
        s1 = start_end_time(start_time=timezone.now(),end_time=timezone.now())
        s1.save()
        try:
            update_obj = membership.objects.create(id=id,real_name=real_name,tz=tz, activity_period=s1)
            update_obj.save()
            return redirect('/')
        except Exception as e:
            messages.error(request,'Real Name or ID already existed')
            return render(request, 'register.html')
        
        
    return render(request, 'register.html')