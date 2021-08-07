from django.http import HttpResponse
from django.shortcuts import render

def Index(request): 
    return render(request, 'index.html')

def About(request): 
    return render(request, 'about.html')

def Blog(request):
    return render(request, 'blog.html')

def Contacto(request):
    return render(request, 'contact.html')

def Producto(request):
    return render(request, 'product.html')

def Login(request):
    return render(request, 'Login.html')