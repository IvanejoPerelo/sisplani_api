from .serializers import EmpleadosSerializer
from .models import Empleados
from rest_framework.viewsets import ModelViewSet

class EmpleadosViewSet(ModelViewSet):
    queryset = Empleados.objects.all()
    serializer_class = EmpleadosSerializer