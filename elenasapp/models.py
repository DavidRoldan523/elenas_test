from django.db import models
from django.utils.translation import ugettext as _


class User(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.id

    @property
    def is_authenticated(self):
        return bool(self._token)

    @property
    def user_id(self):
        return self._token.get('user_id', None) if hasattr(self, '_token') else None
