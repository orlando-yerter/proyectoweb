from django.db import models

# Create your models here

class venta(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="tienda")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    class meta:
        vervose_name= "venta"
        vervose_name_plural= "ventas"
    
    def __str__(self):
        return self.titulo



