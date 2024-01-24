from .models import Planillas
from rest_framework.serializers import ModelSerializer
from .models import DetallePlanillas


class PlanillasSerializer(ModelSerializer):
    class Meta: 
        model = Planillas
        fields = "__all__"

class DetallePlanillasSerializer(ModelSerializer):
    class Meta:
        model = DetallePlanillas
        fields = "__all__"