from .views import EmpleadosViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'empleados', EmpleadosViewSet)

urlpatterns = [
    path('',include(router.urls))
]