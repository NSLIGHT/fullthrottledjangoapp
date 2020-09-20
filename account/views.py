from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from account.models import member,membership,start_end_time
from datetime import datetime
from django.utils import timezone
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
    if member.objects.filter(real_name=request.POST['real_name']).exists():
        obj = member.objects.get(real_name=request.POST['real_name'])
        id = obj.id
        real_name = obj.real_name
        tz = obj.tz
        s1 = start_end_time(start_time=timezone.now(),end_time=timezone.now())
        s1.save()
        try:
            update_obj = membership.objects.create(id=id,real_name=real_name,tz=tz, activity_period=s1)
            update_obj.save()
            return render(request, 'login.html')
        except Exception as e:
            print(e)
            return redirect('/')
    else:
        return redirect('/')