from django.db import models
from empleados.models import Empleados



class Planillas (models.Model):
    mes=models.CharField(max_length=10)
    anio=models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta():
        db_table = "planillas"   

class DetallePlanillas(models.Model):
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    planilla = models.ForeignKey(Planillas, on_delete=models.CASCADE)

    class Meta():
        db_table = "detalle_planillas"   