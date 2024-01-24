from .views import EmpleeadosViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'empleados', EmpleeadosViewSet)

urlpatterns = [
    path('',include(router.urls))
]