from django.db.models import query
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
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

def contactar(request):
    if request.method == "POST":
        nombre = request.POST["Nombre"]
        correo = request.POST["Email"]
        telefono = request.POST["Phone"]
        mensaje = request.POST["Mensaje"]
        mensajeT = "Hola!! Soy "+nombre+"\n-Mi correo es: "+correo+"\n-Mi numero es "+telefono+"\n\nMENSAJE\n\n"+mensaje
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["benanxio@gmail.com"]
        send_mail("Quiero más información", mensajeT, email_desde, email_para, fail_silently=False)
        productos = Producto.objects.all()
        return render(request, 'product.html',{'Productos': productos})
    
    return render(request, "contact.html")