from django.urls import path, include

from . import views


urlpatterns = [
    path('employers/', views.EmployerViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('tasks/', views.TaskViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('tasks/<int:pk>/', views.TaskViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
]