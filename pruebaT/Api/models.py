from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Eventos(models.Model):
    idEvento = models.AutoField(primary_key=True,unique=True,verbose_name="Codigo Envento")
    nombre = models.CharField(max_length=150,verbose_name="Nombre del Evento")
    tipo = models.CharField(choices=(("Tipo1", "Tipo1"),("Tipo2", "Tipo2")),max_length=5,verbose_name="Tipo de Evento")
    descripcion = models.CharField(max_length=150,verbose_name="Descripcion del Evento")
    fecha = models.DateTimeField(verbose_name="Fecha del Evento")
    estado = models.CharField(choices=(("Pendiente por revisar", "Pendiente por revisar"),("Revisado", "Revisado")), max_length=35,verbose_name="Estado del Evento",default="Pendiente por revisar")
    gestion = models.CharField(choices=(("Requiere gestión", "Requiere gestión"),("Sin gestión", "Sin gestión")),max_length=35,verbose_name="Proceso de Gestión",blank=True,null=True)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Usuario Responsable")
    eliminado = models.BooleanField(default=False)
    

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['nombre']

    def __str__(self):
        return str(self.nombre)

class logEvento(models.Model):
    idLog = models.AutoField(primary_key=True,unique=True,verbose_name="Codigo Log Envento")
    idEvento = models.ForeignKey(Eventos,on_delete=models.CASCADE,verbose_name="Evento")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Acción")
    accion = models.CharField(choices=(("Creado", "Creado"),("Modificado", "Modificado"),("Eliminado", "Eliminado")), max_length=20,verbose_name="Acción Realizada",null=True,blank=True)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Usuario Responsable")

    class Meta:
        verbose_name = 'Log Evento'
        verbose_name_plural = 'Logs Eventos'

    def __str__(self):
        return str(self.accion)
    