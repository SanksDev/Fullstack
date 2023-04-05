from django.db import models

# Create your models here.

class Publicacion(models.Model):
    codigo=models.CharField(primary_key=True, max_length=6)
    titulo=models.CharField(max_length=50, verbose_name='Título')
    imagen =models.ImageField(upload_to='imagenes/', verbose_name="Imagen", null=True)
    descrip=models.CharField(max_length=500, verbose_name="Descripción")


    def __str__(self):  
        fila = "Título: " + self.titulo + " - " + "Descripción: " + self.descrip
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        return super().delete()