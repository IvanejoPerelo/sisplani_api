from django.contrib import admin
from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('afp/', index),
#     path('aportaciones/', index),
#     path('descuentos/', index),
#     path('empleados/', index),
# ]

api_version = "api/v1/"

urlpatterns = [
    path('admin/', admin.site.urls),
    path(api_version, include("afp.urls")),
]