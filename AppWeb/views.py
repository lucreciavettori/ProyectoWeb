from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render (request, 'AppWeb/inicio.html')

def clientes(request):
    return render (request, 'AppWeb/clientes.html')

def vendedor(request):
    return render (request, 'AppWeb/vendedor.html')

def auto(request):
    return render (request, 'AppWeb/vehiculo.html')

