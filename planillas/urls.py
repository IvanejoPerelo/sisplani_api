from .views import PlanillasViewSet
from .views import DetallePlanillasViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'planillas', PlanillasViewSet)
router.register(r'detalleplanilla',DetallePlanillasViewSet)

urlpatterns = [
    path('', include(router.urls)), 
]