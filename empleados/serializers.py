from rest_framework.serializers import ModelSerializer
from .models import Empleados

class EmpleadosSerializer(ModelSerializer):
    class Meta:
        model = Empleados
        fields = "__all__"