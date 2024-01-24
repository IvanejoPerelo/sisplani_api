from .models import Descuentos
from .serializers import DescuentosSerializer
from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated

class DescuentosViewSet(ModelViewSet):
    queryset = Descuentos.objects.all()
    serializer_class = DescuentosSerializer
    # permission_classes = [IsAuthenticated]