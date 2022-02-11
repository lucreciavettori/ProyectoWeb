from django.urls import path
from AppWeb.views import buscar, busquedavehiculo, vehiculo, cliente, inicio, vendedor

urlpatterns = [
    path('cliente/', cliente),
    path('vendedor/', vendedor),
    path('vehiculo/', vehiculo),
    path('inicio/', inicio),
    path('buscar/', buscar),
    path('busquedavehiculo/', busquedavehiculo),
]
