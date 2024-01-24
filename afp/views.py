from .models import Afp
from .serializers import AfpSerializer
from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated

class AfpViewSet(ModelViewSet):
    queryset = Afp.objects.all()
    serializer_class = AfpSerializer
    # permission_classes = [IsAuthenticated]
