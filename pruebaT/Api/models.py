from django.db import models

# Create your models here.
class Productos(models.Model):
    idProducto = models.AutoField(primary_key=True,unique=True,verbose_name="Codigo Producto")
    nombre = models.CharField(max_length=150,verbose_name="Nombre Producto")
    descripcion = models.TextField(max_length=250, verbose_name="Descripcion Producto")
    precio = models.IntegerField(default=0, verbose_name="Precio Producto")

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']

    def __str__(self):
        return str(self.nombre)

class DetalleProductos(models.Model):
    idDetalleProducto = models.AutoField(primary_key=True,unique=True,verbose_name="Detalle Producto")
    idProducto = models.ForeignKey(Productos, on_delete=models.CASCADE, verbose_name="Producto")
    cantidad = models.IntegerField(default=1,verbose_name="Cantidad Producto")
    valorTotal = models.FloatField(verbose_name="Valor Total",default=0,blank=True)
    valorIva = models.FloatField(verbose_name="Valor IVA",default=0,blank=True)

    class Meta:
        verbose_name = 'Detalle del Producto'
        verbose_name_plural = 'Detalles de Productos'
        ordering = ['idProducto']

    def __str__(self):
        return str(self.idProducto.nombre)
    