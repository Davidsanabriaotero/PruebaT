from .models import *
from rest_framework import serializers

class ProductosSerializer(serializers.ModelSerializer):
  class Meta:
    model = Productos
    fields = '__all__'

class DetallesProductosSerializer(serializers.ModelSerializer):
  class Meta:
    model = DetalleProductos
    fields = ('idDetalleProducto','idProducto','cantidad','valorTotal','valorIva')
    read_only_fields = ('valorTotal','valorIva')
  
