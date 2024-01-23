from django.db import models
from planillas.models import DetallePlanillas

class Ingresos(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion = models.TextField(null=True)
    periodo=models.PositiveIntegerField()
    monto=models.FloatField
    detallePlanilla = models.ForeignKey(DetallePlanillas, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nombre
    
    class Meta():
        db_table = "ingresos"