from django.contrib import admin

# Register your models here.

from account.models import member, membership


admin.site.register(member)
admin.site.register(membership)