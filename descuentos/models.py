from django.db import models

class Descuentos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField
    tipo = models.CharField(max_length=10)
    monto = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nombre
    
    class Meta():
        db_table = "descuentos"