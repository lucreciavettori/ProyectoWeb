from django.urls import path
from AppWeb.views import buscar, busquedavehiculo, vehiculo, cliente, inicio, vendedor

urlpatterns = [
    path('cliente/', cliente,name="Cliente"),
    path('vendedor/', vendedor, name="Vendedor"),
    path('vehiculo/', vehiculo, name="Vehiculo"),
    path('inicio/', inicio, name="Inicio"),
    path('buscar/', buscar),
    path('busquedavehiculo/', busquedavehiculo,name="Buscar"),
]
