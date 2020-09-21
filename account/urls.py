from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
# app_name = 'account'

urlpatterns = [
    path('', views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
] 