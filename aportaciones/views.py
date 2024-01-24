from .models import Aportaciones
from .serializers import AportacionesSerializer
from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated

class AportacionesViewSet(ModelViewSet):
    queryset = Aportaciones.objects.all()
    serializer_class = AportacionesSerializer
    # permission_classes = [IsAuthenticated]

