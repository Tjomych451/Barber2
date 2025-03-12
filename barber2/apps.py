from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class Barber2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'barber2'
    verbose_name = _('Барбершоп')
