from .views import AfpViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'afp',AfpViewSet)

urlpatterns = [
    path('',include(router.urls))
]