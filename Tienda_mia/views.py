from django.http import HttpResponse
from django.shortcuts import render
from Tienda_mia.Aplicaciones.Tienda.models import Producto

def Index(request): 
    return render(request, 'index.html')

def About(request): 
    return render(request, 'about.html')

def Blog(request):
    return render(request, 'blog.html')

def Contacto(request):
    return render(request, 'contact.html')

def Productos(request):

    productos = {'Productos': Producto.objects.all()}

    return render(request, 'product.html',productos)

def Login(request):
    return render(request, 'Login.html')