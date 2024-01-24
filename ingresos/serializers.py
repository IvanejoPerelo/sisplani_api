from rest_framework.serializers import ModelSerializer
from .models import Ingresos

class IngresosSerializer(ModelSerializer):
    class Meta:
        model = Ingresos
        fields = "__all__"