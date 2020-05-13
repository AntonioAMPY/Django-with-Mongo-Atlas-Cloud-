from django.db import models

# Create your models here.
class Personas(models.Model):
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 50)
    telefono = models.IntegerField()
    correo = models.CharField(max_length= 20)

    def __str__(self):
        return self.nombre