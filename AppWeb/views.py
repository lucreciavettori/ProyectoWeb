from django.shortcuts import render

# Create your views here.
def clientes(request):
    return render (request, 'AppWeb/index.html')

def vendedor(request):
    return render (request, 'AppWeb/vendedor.html')

def auto(request):
    return render (request, 'AppWeb/vehiculo.html')