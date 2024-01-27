from .serializers import PlanillasSerializer, DetallePlanillasSerializer
from .models import Planillas
from .models import DetallePlanillas
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from empleados.models import Empleados
from empleados.serializers import EmpleadosSerializer
from valores.models import Valores
from valores.serializers import ValoresSerializer
from afp.models import Afp
from afp.serializers import AfpSerializer
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
        afps = Afp.objects.all()


        empleados = []
        total_general = []

        for detalle in detalles:
            detalle_serializer = DetallePlanillasSerializer(detalle).data
            #print (detalle_serializer)
            empleado = EmpleadosSerializer(Empleados.objects.get(
                pk=detalle_serializer["empleado"])).data
            
            afp_empleado = empleado["afp"] #Aqui estoy asignado a la variable afp_empleado el id de su afp           
            
            #Variables Globales
            total = empleado["remuneracion"]
            remuneracion = empleado["remuneracion"]
            sueldo_bruto = 0
            sueldo_neto = 0

            #Variables Ingresos
            ingresos = []
            total_ingresos = 0

            #Variables Descuentos
            descuentos = []
            total_descuentos = 0

            #Variables Aportaciones
            Aportaciones = []
            total_aportaciones = 0

            #Variables Afp
            base_aportacion = 0
            calculo_aportes = 0
            calculo_seguro = 0
            calculo_comision = 0
            total_afp = 0
            maxRemuneracion = 0


            for valor in detalle_serializer["valores"]:
                valor_data = ValoresSerializer(Valores.objects.get(pk=valor))
                #Sprint("valor_monto:", valor_data["monto"].value) 
                
                if (valor_data["tipo"].value == 1):
                    total_ingresos += valor_data["monto"].value
                    #total += valor_data["monto"].value
                    ingresos.append({
                        "nombre":valor_data["nombre"],
                        "monto":valor_data["monto"]
                    })

                if (valor_data["tipo"].value == 2):
                    total_descuentos += valor_data["monto"].value
                    #total -= valor_data["monto"].value
                    descuentos.append({
                        "nombre":valor_data["nombre"],
                        "monto":valor_data["monto"]
                    })                
                
                if (valor_data["tipo"].value == 3):
                    aportacion = valor_data["monto"].value * empleado["remuneracion"]

            sueldo_bruto = remuneracion + total_ingresos
            afp_elegido = AfpSerializer(Afp.objects.get(
            pk=afp_empleado)).data

            maxRemuneracion=afp_elegido["maxRemuneracion"]

            if (sueldo_bruto > maxRemuneracion):
                base_aportacion = maxRemuneracion
            else:
                base_aportacion = sueldo_bruto

            calculo_aportes = base_aportacion * afp_elegido["tasaAportes"]
            calculo_seguro = base_aportacion * afp_elegido["tasaSeguros"]         
            calculo_comision = base_aportacion * afp_elegido["tasaComisionVariable"]         
            total_afp = calculo_aportes + calculo_seguro + calculo_comision
            sueldo_neto = sueldo_bruto - total_descuentos - total_afp

            empleados.append({
                "empleado": empleado,
                "remuneracion": remuneracion,
                "total_ingresos": total_ingresos,
                "sueldo_bruto": sueldo_bruto,   
                "aportacion": aportacion,            
                "total_descuentos": total_descuentos,
                "aportes_afp": calculo_aportes,
                "seguro_afp": calculo_seguro,
                "comision_afp": calculo_comision,
                "total_afp": total_afp,
                "sueldo_neto": sueldo_neto
            })

        suma_remuneracion=0
        suma_total_ingresos = 0
        suma_sueldo_bruto = 0
        suma_total_descuentos =0
        suma_total_afp = 0
        suma_sueldo_neto = 0

        for items in empleados:
            suma_remuneracion += items["remuneracion"]
            suma_total_ingresos += items["total_ingresos"]
            suma_sueldo_bruto += items["sueldo_bruto"]
            suma_total_descuentos += items["total_descuentos"]
            suma_total_afp +=items["total_afp"]
            suma_sueldo_neto +=items["sueldo_neto"]


        return Response({
            "ok": True,
            "data": empleados,
        })
    
