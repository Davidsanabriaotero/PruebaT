from django.urls import path, include
from Api import views
from rest_framework import routers

#Declaración del routers
ruta = routers.DefaultRouter()

#Incorporación de las viewSet y Registración de los Router
ruta.register('Productos', views.ProductosViewSet,'Productos')
ruta.register('DetallesProductos', views.DetallesProductosViewSet,'DetallesProductos')

urlpatterns = ruta.urls


