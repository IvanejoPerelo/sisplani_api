from .models import Ingresos
from .serializers import IngresosSerializer
from rest_framework.viewsets import ModelViewSet

class IngresosViewSet(ModelViewSet):
    queryset = Ingresos.objects.all()
    serializer_class = IngresosSerializer