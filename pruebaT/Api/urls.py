from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventosViewSet,LogEventosViewSet

rutas = DefaultRouter()
rutas.register(r'eventos', EventosViewSet)
rutas.register(r'logeventos', LogEventosViewSet)

urlpatterns = [
    path('api/', include(rutas.urls)),
]

