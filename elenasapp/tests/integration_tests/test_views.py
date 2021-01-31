import pytest

from django.test import RequestFactory
from rest_framework.test import force_authenticate
from rest_framework import status

from elenasapp.views import (EmployerViewSet, TaskViewSet,) 
from elenasapp.models import (Employer, Task,) 
from django.contrib .auth.models import User


@pytest.fixture
def user_authenticated(db) -> User:
    user = User.objects.create(
        username="test",
        first_name="test",
        last_name="test",
        password="test123",
        email="test@mail.com"
    )
    return user


@pytest.fixture
def employer(db, user_authenticated: User) -> Employer:
    return Employer.objects.create(
        owner=user_authenticated, name="test-employer"
    )


@pytest.fixture
def task(db, employer: Employer) -> Task:
    return Task.objects.create(
        title="test-task",
        description="test-description",
        employer=employer
    )


def test_employers_list(rf: RequestFactory, user_authenticated: User):
    request = rf.get('employers/')
    force_authenticate(request, user=user_authenticated)
    view = EmployerViewSet.as_view({'get': 'list'})
    response = view(request)
    assert response.status_code == status.HTTP_200_OK

def test_tasks_list(rf: RequestFactory, user_authenticated: User):
    request = rf.get('tasks/')
    force_authenticate(request, user=user_authenticated)
    view = TaskViewSet.as_view({'get': 'list'})
    response = view(request)
    assert response.status_code == status.HTTP_200_OK

def test_task_retrieve(rf: RequestFactory, user_authenticated: User,
                       task: Task):
    request = rf.get('tasks/<int:pk>/')
    force_authenticate(request, user=user_authenticated)
    view = TaskViewSet.as_view({'get': 'retrieve'})
    response = view(request, pk=task.pk)
    assert response.status_code == status.HTTP_200_OK

def test_task_delete(rf: RequestFactory, user_authenticated: User,
                     task: Task):
    request = rf.delete('tasks/<int:pk>/')
    force_authenticate(request, user=user_authenticated)
    view = TaskViewSet.as_view({'delete': 'destroy'})
    response = view(request, pk=task.pk)
    assert response.status_code == status.HTTP_200_OK

def test_task_create(rf: RequestFactory, user_authenticated: User,
                     employer: Employer):
    request = rf.post(
        'tasks/',
        {
            'title': "New task test",
            'description': "New description",
            'employer': employer
        }
    )
    force_authenticate(request, user=user_authenticated)
    view = TaskViewSet.as_view({'post': 'create'})
    response = view(request)
    assert response.status_code == status.HTTP_201_CREATED

def test_employer_create(rf: RequestFactory, user_authenticated: User):
    request = rf.post(
        'employers/',
        {
            'name': "test-employer",
            'owner': user_authenticated
        }
    )
    force_authenticate(request, user=user_authenticated)
    view = EmployerViewSet.as_view({'post': 'create'})
    response = view(request)
    assert response.status_code == status.HTTP_201_CREATED
