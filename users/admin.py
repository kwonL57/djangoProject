from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(UsersModel)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_email',
        'user_pw',
        'user_name',
        'user_area',
        #'create_time',
    )