from rest_framework.serializers import ModelSerializer
from .models import Empleados

class EmpleleadosSerializer(ModelSerializer):
    class Meta:
        model = Empleados
        fields = "__all__"