from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User  # Your custom user model
        fields = ('email', 'emp_name', 'password')

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            emp_name=validated_data['emp_name'],
        )
        user.set_password(validated_data['password'])  # Important!
        user.save()
        return user
