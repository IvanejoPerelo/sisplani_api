from django.db import models
from empleados.models import Empleados
from valores.models import Valores



class Planillas (models.Model):
    fecha_planilla = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    

    class Meta():
        db_table = "planillas"   

class DetallePlanillas(models.Model):
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    planilla = models.ForeignKey(Planillas, on_delete=models.CASCADE)
    valores = models.ManyToManyField(Valores, blank=True, null=True)
    subtotal = models.FloatField()
    total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta():
        db_table = "detalle_planillas"   