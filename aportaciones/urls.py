from .views import AportacionesViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'aportaciones',AportacionesViewSet)
urlpatterns = [
    path('',include(router.urls))
]