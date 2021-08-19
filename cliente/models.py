from django.db import models
import re
# Create your models here.
class ClienteManager(models.Manager):
        #agregar dentro del modelo para realizar validaciones
        def validador_cliente(self,dato):
            errores = {}
            if len(dato['nombre']) == 0:    
                errores['nombre'] = 'Ingrese un nombre'
            if len(dato['apellido']) == 0:    
                errores['apellido'] = 'Ingrese un apellido'
            if len(dato['rut']) == 0:    
                errores['rut'] = 'Ingrese un rut'   
            EMAIL = re.compile(
                r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #expresion regular
            if not EMAIL.match(dato['email']):
                errores['email'] = "email invalido"
            if len(dato['direccion']) == 0:
                errores['direccion'] = 'Ingrese un direccion'
            return errores
        


class  Cliente(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    apellido = models.CharField(max_length=50,verbose_name='Apellido')
    rut = models.CharField(max_length=12,verbose_name='Rut')
    email = models.CharField(max_length=150,verbose_name='Email')
    password = models.CharField(max_length=50,verbose_name='Password')
    direccion = models.CharField(max_length=50,verbose_name='Direccion')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Fecha Actualizacion')
    objects = ClienteManager()