from django.apps import AppConfig
from django.db.models.signals import post_save, pre_save

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Api'

    def ready(self):
        from .models import DetalleProductos
        from .receivers import calcularValoresPreSave


        #PRE_SAVE()
        pre_save.connect(calcularValoresPreSave, sender=DetalleProductos)

