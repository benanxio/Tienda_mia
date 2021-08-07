from django.db import models

class Carrito(models.Model):
    id_carrito = models.IntegerField(primary_key=True)
    id_cliente = models.ForeignKey('Clientes', models.DO_NOTHING, db_column='id_cliente')
    cantidad = models.IntegerField(db_column='Cantidad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CARRITO'


class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)

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
    fecha = models.TextField(db_column='Fecha')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'CLIENTES'


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
    fecha = models.TextField(db_column='Fecha')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'EMPLEADOS'


class Fabricante(models.Model):
    id_fabricante = models.AutoField(primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=30)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FABRICANTE'


class MetodoPago(models.Model):
    id_metodo_pago = models.IntegerField(primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'METODO_PAGO'


class NivelUser(models.Model):
    id_nivel = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'NIVEL_USER'


class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_categoria')
    id_fabricante = models.ForeignKey(Fabricante, models.DO_NOTHING, db_column='id_fabricante')
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    imagen = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'PRODUCTO'


class Ubicacion(models.Model):
    departamento = models.CharField(db_column='Departamento', max_length=30)  # Field name made lowercase.
    ciudad = models.CharField(db_column='Ciudad', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UBICACION'


class Venta(models.Model):
    id_venta = models.IntegerField(primary_key=True)
    id_cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    total = models.CharField(db_column='Total', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fecha_venta = models.DateField(db_column='FECHA_VENTA')  # Field name made lowercase. This field type is a guess.
    direccion = models.CharField(db_column='Direccion', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VENTA'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
