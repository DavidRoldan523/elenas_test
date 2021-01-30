from django.contrib import admin
from django.urls import path, include

from elenasapp.views import health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('elenasapp.urls')),
    path('api/auth/', include('authentication.urls')),

    path('health-check/', health_check, name="health-check"),
]
