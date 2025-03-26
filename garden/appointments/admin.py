from django.contrib import admin
from .models import Service, Master, Visit

@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'contact_info']
    list_filter = ['services']
    search_fields = ['first_name', 'last_name']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'master', 'service', 'created_at']
    list_filter = ['master', 'service', 'created_at']
    search_fields = ['name', 'phone']
