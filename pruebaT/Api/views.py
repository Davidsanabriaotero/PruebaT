from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import *

class EventosViewSet(viewsets.ModelViewSet):
    queryset = Eventos.objects.filter(eliminado=False)
    serializer_class = EventosSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['usuario'] = request.user
        serializer.save()
        return Response(serializer.data)
    
    # GET /eventos/{idEvento}/
    def retrieve(self, request, pk=None):
        queryset = self.get_queryset().exclude(eliminado=True)
        Evento = generics.get_object_or_404(queryset, pk=pk)
        serializer = EventosSerializer(Evento)
        return Response(serializer.data)
    
    # PUT /eventos/{idEvento}/
    def update(self, request, pk=None):
        queryset = self.get_queryset().exclude(eliminado=True)
        Evento = generics.get_object_or_404(queryset, pk=pk)
        serializer = EventosSerializer(Evento, data=request.data)
        if serializer.is_valid():
            serializer.validated_data['usuario'] = request.user
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
    
    # DELETE /eventos/{idEvento}/
    def destroy(self, request, pk=None):
        queryset = self.get_queryset().exclude(eliminado=True)
        Evento = generics.get_object_or_404(queryset, pk=pk)
        Evento.eliminado = True
        Evento.usuario = request.user
        Evento.save()
        return Response(status=204)
    
    # PATCH /eventos/{idEvento}/cambiar_estado/
    @action(detail=True, methods=['pacht','get'])
    def cambiar_estado(self, request, pk=None):
        queryset = self.get_queryset().exclude(eliminado=True)
        Evento = generics.get_object_or_404(queryset, pk=pk)
        serializer = EventosSerializer(Evento)
        if serializer.data.get('estado') == "Pendiente por revisar":
            Evento.estado = "Revisado"
            Evento.save()
            return Response({'message': 'Estado actualizado correctamente'})
        else:
            return Response({'message': 'Este Evento ya ha sido Revisado'})
    
    
    @action(detail=False, methods=['get'])
    def eventos_Requieren_Gestion(self, request):
        queryset = self.get_queryset().filter(gestion="Requiere gestión",eliminado=False)
        serializer = EventosSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def eventos_Sin_Gestion(self, request):
        queryset = self.get_queryset().filter(gestion="Sin gestión",eliminado=False)
        serializer = EventosSerializer(queryset, many=True)
        return Response(serializer.data)

class LogEventosViewSet(viewsets.ModelViewSet):
    queryset = logEvento.objects.all()
    serializer_class = LogsEventosSerializer

    