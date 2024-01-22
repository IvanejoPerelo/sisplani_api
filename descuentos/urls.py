from .views import DescuentosViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'descuentos',DescuentosViewSet)

urlpatterns = [
    path('', include(router.urls))
]