from django.contrib import admin
from django.urls import path
from afp.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('afp/', index),
    path('aportaciones/', index),
    path('descuentos/', index),
    path('empleados/', index),
]
