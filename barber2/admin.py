from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'date', 'status')
    list_display_links = ('name', 'phone')
    search_fields = ('name', 'phone')
    list_filter = ('status', 'date')
    list_editable = ('status',)
    date_hierarchy = 'date'

    actions = ['approve_appointment', 'reject_appointment']

    def approve_appointment(self, request, queryset):
        queryset.update(status='approved')
    approve_appointment.short_description = _('Одобрить выбранные записи')

    def reject_appointment(self, request, queryset):
        queryset.update(status='rejected')
    reject_appointment.short_description = _('Отклонить выбранные записи')
