from django.urls import path, include

from . import views


urlpatterns = [
    path('users/', views.UserViewSet.as_view({'get': 'list', 'post': 'create'})),
]