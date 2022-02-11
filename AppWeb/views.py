from django.shortcuts import render
from AppWeb.forms import ClientesFormulario, VehiculoFormulario,VendedorFormulario
from AppWeb.models import Auto, Clientes, Vendedor

# Create your views here.
def inicio(request):
    return render (request, 'AppWeb/inicio.html')

#def clientes(request):
    #return render (request, 'AppWeb/clientes.html')

#def vendedor(request):
    #return render (request, 'AppWeb/vendedor.html')

#def auto(request):
    #return render (request, 'AppWeb/vehiculo.html')

def cliente(request):
    
    if request.method == 'POST':
        
        miFormulario = ClientesFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.data
            
            r_nombre = informacion['nombre']
            r_apellido = informacion['apellido']
            r_email = informacion['email']
        
            cliente = Clientes(nombre=r_nombre, apellido=r_apellido, email=r_email)
            cliente.save()
    
    miFormulario = ClientesFormulario()

    return render(request, 'AppWeb/clientes.html', {"miFormulario": miFormulario})

def vendedor(request):
    
    if request.method == 'POST':
        
        miFormulario = VendedorFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.data
            
            r_nombre = informacion['nombre']
            r_apellido = informacion['apellido']
            r_legajo = informacion['legajo']
        
            vendedor = Vendedor(nombre=r_nombre, apellido=r_apellido, legajo=r_legajo)
            vendedor.save()
    
    miFormulario = VendedorFormulario()

    return render(request, 'AppWeb/vendedor.html', {"miFormulario": miFormulario})

def vehiculo(request):
    
    if request.method == 'POST':
        
        miFormulario = VehiculoFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.data
            
            r_marca = informacion['marca']
            r_modelo = informacion['modelo']
            r_añofabricacion = informacion['añofabricacion']
            r_disponible = informacion['disponible']
        
            vehiculo = Auto(marca=r_marca, modelo=r_modelo, añofabricacion=r_añofabricacion, disponible=r_disponible)
            vehiculo.save()
    
    miFormulario = VehiculoFormulario()

    return render(request, 'AppWeb/vehiculo.html', {"miFormulario": miFormulario})

def buscar(request):
    
    if request.GET['marca']:
        marca =request.GET ['marca']
        vehiculo =Auto.objects.filter(marca__icontains=marca)
    
        return render(request, 'AppWeb/resultadoporbusqueda.html', { "vehiculo": vehiculo,"marca": marca })
    else:

        respuesta ="No enviar datos"

    return render(request, 'AppWeb/resultadoporbusqueda.html')


def busquedavehiculo(request):
    return render(request, 'AppWeb/busquedavehiculo.html' )