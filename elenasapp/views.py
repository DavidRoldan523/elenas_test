from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.serializers import BaseSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from . import models
from . import serializers


class EmployerViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = serializers.EmployerSerializer
    queryset = models.Employer.objects.exclude(owner__username='root')

    def get_queryset(self):
        return self.queryset.filter()


class TaskViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()

    def get_queryset(self):
        return self.queryset.filter()


@api_view(['GET'])
@authentication_classes(())
@permission_classes([])
def health_check(request):
    return Response({'result': 'ok'})