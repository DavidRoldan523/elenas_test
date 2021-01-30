from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.serializers import BaseSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from utils.pagination import BasicPagination, BasicPaginationHandlerMixin
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from . import models
from . import serializers


class EmployerViewSet(ModelViewSet, BasicPaginationHandlerMixin):
    permission_classes = [IsAuthenticated]
    pagination_class = BasicPagination
    serializer_class = serializers.EmployerSerializer
    queryset = models.Employer.objects.exclude(owner__username='root')

    def get_queryset(self):
        return self.queryset.filter()


class TaskViewSet(ModelViewSet, BasicPaginationHandlerMixin):
    permission_classes = [IsAuthenticated]
    pagination_class = BasicPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['description']
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()

    def get_queryset(self):
        return self.queryset.filter()

    def update(self, request, *args, **kwargs):
        task = self.get_object()

        if request.data:
            if task.check_owner(task, self.request.user):
                serializer = self.get_serializer(
                    task, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                response = Response(serializer.data, status=status.HTTP_200_OK)
            else:
                response = Response({'error': 'Unauthorized action'},
                                    status=status.HTTP_401_UNAUTHORIZED)
        else:
            response = Response({'error': 'Missing field(s)'},
                                status=status.HTTP_400_BAD_REQUEST)
        return response


@api_view(['GET'])
@authentication_classes(())
@permission_classes([])
def health_check(request):
    return Response({'result': 'ok'})