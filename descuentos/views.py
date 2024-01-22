from .models import Descuentos
from .serializers import DescuentosViewSet
from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated

class DescuentosViewSet(ModelViewSet):
    queryset = Descuentos.objects.all()
    serializer_class = DescuentosViewSet
    # permission_classes = [IsAuthenticated]