from django.db import models
from afp.models import Afp
from django.contrib.auth.models import User

class Empleados(models.Model):
    dni = models.CharField(max_length=8)
    apellidoPaterno = models.CharField(max_length=20, null=True, db_column="apellido_paterno")
    apellidoMaterno = models.CharField(max_length=20, null=True, db_column="apellido_materno")
    nombres = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    direccion = models.TextField,
    regimenLaboral = models.CharField(max_length=20, null=True, db_column="regimen_laboral")
    categoriaOcupacional=models.CharField(max_length=20, null=True, db_column="categoria_ocupacional")
    cargo = models.CharField(max_length=50)
    fechaIngreso=models.DateField(null=True, db_column="fecha_ingreso")
    remuneracion = models.FloatField()
    estado = models.BooleanField(null=True)
    afp = models.OneToOneField(Afp, on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.apellido_paterno} {self.apellido_materno}, {self.nombres}"

    class Meta():
        db_table = "empleados"   
