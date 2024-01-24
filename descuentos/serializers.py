from rest_framework.serializers import ModelSerializer
from .models import Descuentos

class DescuentosSerializer(ModelSerializer):
    class Meta:
        model = Descuentos
        fields = "__all__"