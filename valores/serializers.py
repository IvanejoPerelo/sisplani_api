from rest_framework.serializers import ModelSerializer
from .models import Valores

class ValoresSerializer(ModelSerializer):
    class Meta:
        model = Valores
        fields = "__all__"