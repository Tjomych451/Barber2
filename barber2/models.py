from django.db import models
from django.utils.translation import gettext_lazy as _

class Appointment(models.Model):
    name = models.CharField(_('Имя клиента'), max_length=100)
    phone = models.CharField(_('Телефон'), max_length=20)
    date = models.DateTimeField(_('Дата записи'))
    status = models.CharField(_('Статус'), max_length=20)
    
    class Meta:
        verbose_name = _('Запись')
        verbose_name_plural = _('Записи')
