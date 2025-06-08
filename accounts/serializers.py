from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from accounts.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'email'
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
