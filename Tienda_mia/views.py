from django.db.models import query
from django.http import HttpResponse
from django.shortcuts import render
from Tienda_mia.Aplicaciones.Tienda.models import Producto

def Index(request): 
    productos = Producto.objects.all()[:4]
    return render(request, 'index.html',{'Productos': productos})

def About(request): 
    return render(request, 'about.html')

def Blog(request):
    return render(request, 'blog.html')

def Contacto(request):
    return render(request, 'contact.html')

def Productos(request):
    queryset = request.GET.get("buscar")

    if queryset:
        productos = Producto.objects.filter(nombre__icontains = queryset)
    
    else:
        productos = Producto.objects.all()

    return render(request, 'product.html',{'Productos': productos})

def Login(request):
    return render(request, 'Login.html')

def DetallesProducto(request,id_producto):
    producto_detalles = {'Productos': Producto.objects.get(id_producto=id_producto)}
    return render(request,'product_details.html',producto_detalles)

def Carrito_c(request):
    return render(request,'Carrito.html')