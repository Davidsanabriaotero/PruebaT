from .models import *

def definirTipoGestion(sender, instance, **kwargs):
    Evento = Eventos.objects.get(idEvento=instance.idEvento)
    if Evento.estado == "Revisado":
        if Evento.gestion == None:
            if Evento.tipo == "Tipo1":  
                Evento.gestion = "Requiere gestión"
                Evento.save()
            else:
                Evento.gestion = "Sin gestión"
                Evento.save()

def crearLogEvento(sender, instance, **kwargs):
    LogEvento = logEvento.objects.filter(idEvento=instance.idEvento)
    if LogEvento:
        Evento = Eventos.objects.get(idEvento=instance.idEvento)
        if Evento.eliminado != True:
            log = logEvento(idEvento=Evento,accion="Modificado", usuario=Evento.usuario)
            log.save()
        else:
            log = logEvento(idEvento=Evento,accion="Eliminado", usuario=Evento.usuario)
            log.save()
    else:
        log = logEvento(idEvento=instance,accion="Creado", usuario=instance.usuario)
        log.save()