
from Tienda_mia.settings import MEDIA_ROOT
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Tienda_mia.views import Index, Login,Productos,About,Blog,Contacto, DetallesProducto,Carrito_c,contactar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index),
    path('Producto/', Productos),
    path('About/',About),
    path('Blog/',Blog),
    path('Contacto/',Contacto),
    path('Login/',Login),
    path('<int:id_producto>/',DetallesProducto),
    path("Carrito/", Carrito_c),
    path("Contactar/", contactar)
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)