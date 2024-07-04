from django.db import models

class Registro(models.model):
    Nombre_Completo = models.CharField(max_length=200)
    Correo_Electronico = models.CharField(max_length=50)
    rut = models.CharField(max_length=50)
    Celular = models.CharField(max_length=10)
    def __str__(self):
        return str(self.Nombre_Completo)

class producto(models.Model):
    Nombre_producto = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio = models.CharField(max_length=10)
    image = models.ImageField(upload_to="images/", default=None)
    def __str__(self):
        return str(self.Nombre_producto)
