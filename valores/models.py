from django.db import models

class Valores(models.Model):

    TIPO_VALOR = [
        (1, 'INGRESOS'),
        (2, 'DESCUENTOS'),
        (3, 'APORTACIONES'),
    ]
        
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    tipo = models.PositiveIntegerField(choices=TIPO_VALOR, default=1)
    monto = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.nombre} - {self.tipo}"
    
    class Meta:
        db_table = "valores"