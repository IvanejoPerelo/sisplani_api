from django.contrib import admin
from django.urls import path, include

api_version = "api/v1/"

urlpatterns = [
    path('admin/', admin.site.urls),
    path(api_version, include("afp.urls")),
    path(api_version, include("aportaciones.urls")),
    path(api_version, include("descuentos.urls")),
    path(api_version, include("empleados.urls")),
    path(api_version, include("ingresos.urls")),
    path(api_version, include("planillas.urls")),
    path(api_version, include("user.urls")),
    path(api_version, include("valores.urls")),
]