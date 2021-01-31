import pytest
from elenasapp.models import (Employer, Task,) 
from django.contrib .auth.models import User


@pytest.fixture
def employer(db) -> Employer:
    owner = User.objects.create(
        username="test",
        first_name="test",
        last_name="test",
        password="test123",
        email="test@mail.com"
    )
    return Employer.objects.create(
        owner=owner, name="test-employer"
    )


@pytest.fixture
def employer_2(db) -> Employer:
    owner = User.objects.create(
        username="test2",
        first_name="test2",
        last_name="test2",
        password="test123",
        email="test2@mail.com"
    )
    return Employer.objects.create(
        owner=owner, name="test2-employer"
    )


@pytest.fixture
def task(db, employer: Employer) -> Task:
    return Task.objects.create(
        title="test-task",
        description="test-description",
        employer=employer
    )


@pytest.fixture
def task_2(db, employer_2: Employer) -> Task:
    return Task.objects.create(
        title="test2-task",
        description="test2-description",
        employer=employer_2
    )


def test_save_task(task: Task):
    task.description = 'New description'
    task.save()
    assert task.description == 'New description'

def test_save_employer(employer: Employer):
    employer.name = 'New name'
    employer.save()
    assert employer.name == 'New name'

def test_delete_task(task: Task):
    task.delete()
    task_remove = Task.objects.filter(pk=task.pk)
    assert not task_remove.exists()

def test_delete_employer(employer: Employer):
    employer.delete()
    employer_remove = Employer.objects.filter(pk=employer.pk)
    assert not employer_remove.exists()

def test_check_owner_task(task: Task, employer: Employer,
                          employer_2: Employer,
                          task_2: Task):
    valid = task.check_owner(task, employer.owner)
    not_valid = task_2.check_owner(task_2, employer.owner)
    assert valid is True
    assert not_valid is False