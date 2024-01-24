from .serializers import EmpleleadosSerializer
from .models import Empleados
from rest_framework.viewsets import ModelViewSet

class EmpleeadosViewSet(ModelViewSet):
    queryset = Empleados.objects.all()
    serializer_class = EmpleleadosSerializer