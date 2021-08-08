from django.db import models
import os

#Directorio
path, filename = os.path.split(os.path.abspath(__file__))
class Carrito(models.Model):
    id_carrito = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey('Clientes', models.DO_NOTHING, db_column='id_cliente')
    cantidad = models.IntegerField(db_column='Cantidad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CARRITO'


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        txt = "[{0}] {1}"
        return txt.format(self.id_categoria,self.nombre)

    class Meta:
        managed = False
        db_table = 'CATEGORIA'


class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=50)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=15)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=15)  # Field name made lowercase.
    dni = models.CharField(db_column='DNI', max_length=8)  # Field name made lowercase.
    sexo = models.CharField(db_column='Sexo', max_length=1)  # Field name made lowercase.
    fecha = models.DateField(auto_now_add=True,db_column='Fecha')  # Field name made lowercase. This field type is a guess.

    def __str__(self):
        txt = "[{0}] {1}"
        return txt.format(self.id_cliente,self.nombre)

    class Meta:
        managed = False
        db_table = 'CLIENTES'


class Empleados(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    id_nivel = models.IntegerField()
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=50)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=15)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=15)  # Field name made lowercase.
    dni = models.CharField(db_column='DNI', max_length=8)  # Field name made lowercase.
    sexo = models.CharField(db_column='Sexo', max_length=1)  # Field name made lowercase.
    fecha = models.DateField(auto_now_add=True,db_column='Fecha')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'EMPLEADOS'


class Fabricante(models.Model):
    id_fabricante = models.AutoField(primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=30)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200)  # Field name made lowercase.

    def __str__(self):
        txt = "[{0}] {1}"
        return txt.format(self.id_fabricante,self.nombre)
        

    class Meta:
        managed = False
        db_table = 'FABRICANTE'


class MetodoPago(models.Model):
    id_metodo_pago = models.AutoField(primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        txt = "[{0}] {1}"
        return txt.format(self.id_metodo_pago,self.nombre)

    class Meta:
        managed = False
        db_table = 'METODO_PAGO'


class NivelUser(models.Model):
    id_nivel = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'NIVEL_USER'

def cambiar_ruta_de_fichero(instance, filename):
    if os.path.isdir(os.path.join('uploads', instance.titulo)):
        pass
    else:
        os.mkdir(os.path.join('uploads', instance.titulo))
    return os.path.join('uploads', instance.titulo , filename)
    
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_categoria')
    id_fabricante = models.ForeignKey(Fabricante, models.DO_NOTHING, db_column='id_fabricante')
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    descripcion = models.TextField(max_length=200)
    imagen = models.ImageField(upload_to="Productos")

    def __str__(self):
        txt = "[{0}] {1} Precio S/. {2} en stock {3}"
        return txt.format(self.id_producto,self.nombre,self.precio,self.stock)

    class Meta:
        #managed = False
        db_table = 'PRODUCTO'


class Ubicacion(models.Model):
    id_ub = models.AutoField(db_column='id', primary_key=True)
    departamento = models.CharField(db_column='Departamento', max_length=30)  # Field name made lowercase.
    ciudad = models.CharField(db_column='Provincia', max_length=30)  # Field name made lowercase.

    def __str__(self):
        txt = "[{0}] {1}"
        return txt.format(self.departamento,self.ciudad)

    class Meta:
        managed = False
        db_table = 'UBICACION'


class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    total = models.CharField(db_column='Total', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fecha_venta = models.DateField(auto_now_add=True,db_column='FECHA_VENTA')  # Field name made lowercase. This field type is a guess.
    direccion = models.CharField(db_column='Direccion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    id_mpago = models.ForeignKey(MetodoPago, models.DO_NOTHING, db_column='id_mpago')

    class Meta:
        managed = False
        db_table = 'VENTA'

class DetalleVenta(models.Model):
    id_detalle = models.AutoField(db_column='Id_detalle', primary_key=True)  # Field name made lowercase.
    id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='id_venta')
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    subtotal = models.DecimalField(max_digits=11, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'DETALLE_VENTA'
