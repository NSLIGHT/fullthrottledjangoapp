from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
import datetime
from django.contrib.postgres.fields import ArrayField


class member(models.Model):
    id = models.CharField(verbose_name = "id",max_length=100,primary_key=True,unique=True)
    real_name = models.CharField(unique=True,max_length=100)
    tz = models.CharField(max_length=100)

    last_login = models.DateTimeField(default=now,auto_now=False, auto_now_add=False)
    last_logout = models.DateTimeField(default=now,auto_now=False, auto_now_add=False)



    def __str__(self):
        return self.real_name


class start_end_time(models.Model):
    start_time = models.DateTimeField(default=now,auto_now=False, auto_now_add=False,null=True,blank=True,verbose_name="start_time")
    end_time = models.DateTimeField(default=now,auto_now=False, auto_now_add=False,null=True,blank=True,verbose_name="end_time")

    def __str__(self):
        return str(self.start_time) + ", " + str(self.end_time)


class membership(models.Model):
    id = models.CharField(verbose_name = "id",max_length=100,primary_key=True,unique=True)
    real_name = models.CharField(unique=True,max_length=100)
    tz = models.CharField(max_length=100)

    activity_period = models.ForeignKey(start_end_time,on_delete=models.CASCADE)

    def __str__(self):
        return self.real_name



















# class UserManager(BaseUserManager):
#     def create_user(self, id,real_name,password=None):
#         if not id:
#             raise ValueError("User must have a id")
#         if not real_name:
#             raise ValueError("User must have a real name")

#         user = self.model(
#             id = id,
#             real_name = real_name,
#             password = password,
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self,id,real_name,password):
#         user = self.create_user(
#             id = id,
#             real_name = real_name,
#             password = password,
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
        
#         user.save(using=self._db)
#         return user

        
#     def authenticate(self, request, real_name=None, password=None):
#         login_valid = (settings.ADMIN_LOGIN == real_name)
#         pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
#         if login_valid and pwd_valid:
#             try:
#                 user = User.objects.get(real_name=real_name)
#             except User.DoesNotExist:
#                 # Create a new user. There's no need to set a password
#                 # because only the password from settings.py is checked.
#                 user = User(real_name=real_name)
#                 user.is_staff = True
#                 user.is_superuser = True
#                 user.save()
#             return user
#         return None
