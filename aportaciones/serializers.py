from rest_framework.serializers import ModelSerializer
from .models import Aportaciones

class AportacionesViewSet(ModelSerializer):
    class Meta:
        model = Aportaciones
        fields = "__all__"