from django.db import models

# Create your models here.
class Clientes(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Vendedor(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    legajo = models.IntegerField(unique=True, null=False)

class Auto(models.Model):

    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    añofabricacion = models.IntegerField()
    disponible = models.BooleanField()