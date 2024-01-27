from django.db import models
from empleados.models import Empleados
from valores.models import Valores

MES_PLANILLA = [
        (1, 'Enero'),
        (2, 'Febrero'),
        (3, 'Marzo'),
        (4, 'Abril'),
        (5, 'Mayo'),
        (6, 'Junio'),
        (7, 'Julio'),
        (8, 'Agosto'),
        (9, 'Setiembre'),
        (10, 'Octubre'),
        (11, 'Noviembre'),
        (12, 'Diciembre'),
]

class Planillas (models.Model):
    anio=models.PositiveIntegerField(null=True)
    mes =models.PositiveIntegerField(choices=MES_PLANILLA, default=1)
    fecha_planilla = models.DateField()
    suma_total_remuneracion = models.FloatField(null=True)
    suma_total_ingresos = models.FloatField(null=True)
    suma_sueldo_bruto = models.FloatField(null=True)
    suma_total_descuentos = models.FloatField(null=True)
    suma_total_afp = models.FloatField(null = True)
    suma_sueldo_neto = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    

    class Meta():
        db_table = "planillas"   

class DetallePlanillas(models.Model):
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    planilla = models.ForeignKey(Planillas, on_delete=models.CASCADE)
    valores = models.ManyToManyField(Valores, blank=True, null=True)
    total_remuneracion = models.FloatField(null=True)
    total_ingresos = models.FloatField(null=True)
    sueldo_bruto = models.FloatField(null=True)
    total_descuentos = models.FloatField(null=True)
    total_afp = models.FloatField(null = True)
    sueldo_neto = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta():
        db_table = "detalle_planillas"   