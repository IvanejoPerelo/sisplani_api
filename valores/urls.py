from .views import ValoresViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'valores',ValoresViewSet)

urlpatterns = [
    path('', include(router.urls))
]