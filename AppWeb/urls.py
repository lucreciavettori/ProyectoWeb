from django.urls import path
from AppWeb.views import auto, clientes, inicio, vendedor

urlpatterns = [
    path('clientes/', clientes),
    path('vendedor/', vendedor),
    path('vehiculo/', auto),
    path('inicio/', inicio),
]
