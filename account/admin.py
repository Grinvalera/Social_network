from django.contrib import admin
from .models import *


@admin.register(PictureUser)
class PictureUserAdmin(admin.ModelAdmin):
    fields = []

    class Meta:
        model = PictureUser


class PictureUserAdminInLine(admin.TabularInline):
    model = PictureUser
    extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', '_password', 'phone_number')
    list_filter = ('first_name', 'username')

    inlines = [PictureUserAdminInLine]


# Register your models here.
