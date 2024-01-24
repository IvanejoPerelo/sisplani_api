from rest_framework.serializers import ModelSerializer
from .models import Afp

class AfpSerializer(ModelSerializer):
    class Meta: 
        model = Afp
        fields = "__all__"