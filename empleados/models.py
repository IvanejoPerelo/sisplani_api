from django.db import models
from afp.models import Afp
from django.contrib.auth.models import User

class Empleados(models.Model):
    dni = models.CharField(max_length=8)
    apellido_paterno = models.CharField(max_length=20, null=True)
    apellido_materno = models.CharField(max_length=20, null=True)
    nombres = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    direccion = models.TextField,
    regimen_laboral = models.CharField(max_length=20, null=True)
    categoria_ocupacional=models.CharField(max_length=20, null=True)
    cargo = models.CharField(max_length=50)
    fecha_ingreso=models.DateField(null=True)
    remuneracion = models.FloatField()
    estado = models.BooleanField(null=True)
    afp = models.OneToOneField(Afp, on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.nombres}"

    class Meta():
        db_table = "empleados"   
