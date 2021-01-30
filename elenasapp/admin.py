# -*- coding: utf-8 -*-
from django.contrib import admin

from elenasapp import models


@admin.register(models.Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'updated_at', 'created_at')


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'employer', 'completed', 'updated_at', 'created_at')