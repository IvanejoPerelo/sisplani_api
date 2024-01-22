from .models import Afp
from .serializers import AfpViewSet
from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated

class AfpViewSet(ModelViewSet):
    queryset = Afp.objects.all()
    serializer_class = AfpViewSet
    # permission_classes = [IsAuthenticated]
