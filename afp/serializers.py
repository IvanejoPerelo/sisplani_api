from rest_framework.serializers import ModelSerializer
from .models import Afp

class AfpViewSet(ModelSerializer):
    class Meta: 
        model = Afp
        fields = "__all__"