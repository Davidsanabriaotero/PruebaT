from .models import *

def calcularValoresPreSave(sender,instance,**kwargs):
    producto = Productos.objects.get(idProducto=instance.idProducto.idProducto)
    instance.valorTotal += int(instance.cantidad) * int(producto.precio)
    instance.valorIva += (instance.valorTotal * (19/100) + instance.valorTotal)