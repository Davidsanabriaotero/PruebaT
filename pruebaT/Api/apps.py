from django.apps import AppConfig
from django.db.models.signals import post_save,pre_save

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Api'

    def ready(self):
        #Importar Receivers
        from .receivers import definirTipoGestion, crearLogEvento
        #Importar Modelos
        from .models import Eventos

        #Conectar signals
        post_save.connect(definirTipoGestion, sender=Eventos)
        post_save.connect(crearLogEvento, sender=Eventos)
 

