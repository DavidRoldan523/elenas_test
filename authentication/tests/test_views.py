import pytest

from django.test import RequestFactory
from rest_framework.test import force_authenticate
from rest_framework import status

from authentication.views import (RegisterView, LoginView,) 
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


def test_login(rf: RequestFactory, user_authenticated: User):
    request = rf.post(
        'login/',
        {
            "username": "other",
            "password": "other",
        }
    )
    # force_authenticate(request, user=user_authenticated)
    view = LoginView.as_view()
    response = view(request)
    # For token created is invalid credentials
    assert response.status_code == status.HTTP_401_UNAUTHORIZED