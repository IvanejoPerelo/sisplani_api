from .views import IngresosViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'ingresos', IngresosViewSet)

urlpatterns = [
    path('', include(router.urls))
]