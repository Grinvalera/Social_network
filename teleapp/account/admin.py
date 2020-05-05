from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', '_password', 'phone_number')
    list_filter = ('first_name', 'nickname')
# Register your models here.
