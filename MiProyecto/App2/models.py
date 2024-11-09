from django.db import models
from django.utils import timezone

# Creamos las Clases/tablas que tiene el proyecto

class Usuarios(models.Model):                           # 15- aparece en la barra superior  
    nombre_usuario = models.CharField(max_length=30)    
    email_usuario = models.EmailField()

    def __str__(self):                                  
        return f' Nombre_usuario: {self.nombre_usuario}, Email_usuario: {self.email_usuario}'  # 15- cada variable  dela clase

class Productos(models.Model):                          # 15- aparece en la barra superior
    nombre_producto = models.CharField(max_length=30)
    marca_producto = models.CharField(max_length=20)

    def __str__(self):
        return f' Nombre_producto: {self.nombre_producto}, Marca_producto: {self.marca_producto}'

class Ventas_detalles(models.Model):                # 15- aparece en la barra superior
    monto = models.FloatField()
    fecha_venta = models.DateField()
    forma_de_pago = models.CharField(max_length=25)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    def __str__(self):
        return f' Monto: {self.monto}, Fecha_venta: {self.fecha_venta}, Forma_de_pago: {self.forma_de_pago}, Producto: {self.producto}, Usuario: {self.usuario}'
    
class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha_envio =  models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'Mensaje de {self.nombre} - {self.email}'

