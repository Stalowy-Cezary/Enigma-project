from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.

class CustomUser(UserAdmin):
    model = User
    UserAdmin.fieldsets += (('Extra Fields', {'fields': ('role', )}),)

admin.site.register(User, CustomUser)
admin.site.register(Product)
admin.site.register(Order)
