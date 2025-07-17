from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Employee model.

    Converts Employee instances to JSON and vice versa.
    """

    class Meta:
        model = Employee
        fields = '__all__'
        # fields = ['id', 'emp_name', 'email', 'password', 'is_active', 'created_at', 'updated_at']
        extra_kwargs = {
            'password': {'write_only': True},
            'created_at': {'read_only': True, 'format': '%Y-%m-%d %H:%M:%S'},
            'updated_at': {'read_only': True, 'format': '%Y-%m-%d %H:%M:%S'},
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(
            validated_data['password'])  # hash password here
        employee = Employee.objects.create(**validated_data)
        return employee

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(
                validated_data['password'])
        else:
            validated_data.pop('password', None)
        return super().update(instance, validated_data)
