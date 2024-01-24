from .serializers import PlanillasSerializer
from .models import Planillas
from .models import DetallePlanillas
from rest_framework.viewsets import ModelViewSet

class PlanillasViewSet(ModelViewSet):
    queryset = Planillas.objects.all()
    serializer_class = PlanillasSerializer

class DetallePlanillasViewSet(ModelViewSet):
    queryset = DetallePlanillas.objects.all()
    serializer_class = DetallePlanillas