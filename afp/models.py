from django.db import models

class Afp(models.Model):
    nombre = models.CharField(max_length=50)
    tasaAportes = models.FloatField(null=True, db_column="tasa_aportes")
    tasaSeguros = models.FloatField(null=True, db_column="tasa_seguros")
    tasaComisionVariable = models.FloatField(null=True, db_column="tasa_comision_variable")
    maxRemuneracion = models.FloatField(null=True, db_column="max_remuneracion")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta():
        db_table = "afp"
