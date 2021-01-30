from django.db import models

from django.contrib .auth.models import User
from django.utils.translation import ugettext as _


class Employer(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    updated_at = models.DateTimeField('Updated at', auto_now=True)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    class Meta:
        verbose_name = 'Employer'
        verbose_name_plural = 'Employers'

    def __str__(self):
        return self.name

    @property
    def is_authenticated(self):
        return bool(self._token)

    @property
    def user_id(self):
        return self._token.get('user_id', None) if hasattr(self, '_token') else None


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    employer = models.ForeignKey(Employer, models.SET_NULL, null=True,
                                 blank=True, related_name="tasks", help_text="task_id")
    updated_at = models.DateTimeField('Updated at', auto_now=True)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title
