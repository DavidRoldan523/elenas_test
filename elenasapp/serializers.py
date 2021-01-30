import json
from rest_framework import serializers

from . import models
from django.contrib .auth.models import User


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'is_active',)


class EmployerBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employer
        fields = ('id', 'name',)


class EmployerSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(
        many=False, read_only=True)

    class Meta:
        model = models.Employer
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.filter().last()
        validated_data['owner'] = user
        return super().create(validated_data)


class TaskSerializer(serializers.ModelSerializer):
    employer = EmployerBasicSerializer(
        many=False, read_only=True)
    employer_id = serializers.PrimaryKeyRelatedField(
        source='employer', many=False, read_only=True)

    class Meta:
        model = models.Task
        fields = '__all__'

    def create(self, validated_data):
        user = models.Employer.objects.get(owner__username=self.context.get('request').user.username)
        validated_data['employer'] = user
        return super().create(validated_data)

