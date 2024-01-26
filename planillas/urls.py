from .views import PlanillasViewSet, DetallePlanillasViewSet, CalculatePlanilla
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'planillas', PlanillasViewSet)
router.register(r'detalleplanilla',DetallePlanillasViewSet)

urlpatterns = [
    path('', include(router.urls)), 
    path('calculate/', CalculatePlanilla.as_view())
]