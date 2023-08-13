from django.contrib import admin
from .models import UserIP

@admin.register(UserIP)
class UserIPAdmin(admin.ModelAdmin):
    list_display = ('user', 'ip_address', 'timestamp')
