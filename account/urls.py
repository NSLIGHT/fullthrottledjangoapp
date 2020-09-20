from django.urls import path,include
from . import views

# app_name = 'account'

urlpatterns = [
    path('', views.home,name='home'),
    path('login/',views.login,name='login')
]