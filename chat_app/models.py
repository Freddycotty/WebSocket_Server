from django.db import models

# Create your models here.
class Mascota(models.Model):
  nombre = models.CharField('Nombre', max_length=200, null=True)
  mascota_tipo = models.CharField('Tipo de Mascota', max_length=200, null=True)
  raza = models.CharField('Raza', max_length=200, null=True)
  
  
  def __str__(self):
    return self.nombre
  