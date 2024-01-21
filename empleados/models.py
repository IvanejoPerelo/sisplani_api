from django.db import models

class Empleados(models.Model):
    dni = models.CharField(max_length=8)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    nombres = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    direccion = models.TextField,
    regimen_laboral = models.CharField(max_length=10)
    categoria_ocupacional=models.CharField(max_length=20)
    cargo = models.CharField(max_length=50)
    fecha_ingreso=models.DateField()
    remuneracion = models.FloatField()
    estado = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.apellido_paterno} {self.apellido_materno}, {self.nombres}"

    class Meta():
        db_table = "empleados"   
