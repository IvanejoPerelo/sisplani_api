from .models import Aportaciones
from .serializers import AportacionesViewSet
from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated

class AportacionesViewSet(ModelViewSet):
    queryset = Aportaciones.objects.all()
    serializer_class = AportacionesViewSet
    # permission_classes = [IsAuthenticated]

