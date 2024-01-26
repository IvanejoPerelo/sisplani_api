from .models import Valores
from .serializers import ValoresSerializer
from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated

class ValoresViewSet(ModelViewSet):
    queryset = Valores.objects.all()
    serializer_class = ValoresSerializer
    # permission_classes = [IsAuthenticated]
