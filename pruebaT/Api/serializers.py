from .models import *
from rest_framework import serializers

class EventosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventos
        fields = '__all__'
        read_only_fields = ('estado','gestion','eliminado',"usuario")

class LogsEventosSerializer(serializers.ModelSerializer):
    class Meta:
        model = logEvento
        fields = '__all__'
        read_only_fields = ('idEvento','fecha','accion','usuario')
  
