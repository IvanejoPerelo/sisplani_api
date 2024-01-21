from django.db import models

class Afp(models.Model):
    nombre = models.CharField(max_length=50)
    tasa_aportes = models.FloatField()
    tasa_seguros = models.FloatField()
    tasa_comision_variable = models.FloatField()
    max_remuneracion = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta():
        db_table = "afp"
