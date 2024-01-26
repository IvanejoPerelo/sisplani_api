from .serializers import PlanillasSerializer, DetallePlanillasSerializer
from .models import Planillas
from .models import DetallePlanillas
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from empleados.models import Empleados
from empleados.serializers import EmpleleadosSerializer
from valores.models import Valores
from valores.serializers import ValoresSerializer
from rest_framework.response import Response

class PlanillasViewSet(ModelViewSet):
    queryset = Planillas.objects.all()
    serializer_class = PlanillasSerializer

class DetallePlanillasViewSet(ModelViewSet):
    queryset = DetallePlanillas.objects.all()
    serializer_class = DetallePlanillasSerializer


class CalculatePlanilla(APIView):
    def get(self, request):
        detalles = DetallePlanillas.objects.all()

        empleados = []
        total_general = []

        for detalle in detalles:
            detalle_serializer = DetallePlanillasSerializer(detalle).data
            empleado = EmpleleadosSerializer(Empleados.objects.get(
                pk=detalle_serializer["empleado"])).data
            
            
            total = empleado["remuneracion"]
            total_descuentos = 0
            total_ingresos = 0
            aportacion = 0

            for valor in detalle_serializer["valores"]:
                valor_data = ValoresSerializer(Valores.objects.get(pk=valor))
                print("valor_monto:", valor_data["monto"].value) 
                
                if (valor_data["tipo"].value == 1):
                    total_ingresos += valor_data["monto"].value
                    total += valor_data["monto"].value

                if (valor_data["tipo"].value == 2):
                    total_descuentos += valor_data["monto"].value
                    total -= valor_data["monto"].value
                
                if (valor_data["tipo"].value == 3):
                    aportacion = valor_data["monto"].value * empleado["remuneracion"]

            empleados.append({
                "empleado": empleado,
                "total": total,
                "total_descuentos": total_descuentos,
                "total_ingresos": total_ingresos,
                "aportacion": aportacion
            })


        return Response({
            "ok": True,
            "data": empleados
        })