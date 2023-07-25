# from rest_framework import serializers
# from .models import CustomUser

# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['id', 'username', 'email', 'home_address', 'phone_number', 'location']


# # users/serializers.py
from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'home_address', 'phone_number', 'location', 'password']
        extra_kwargs = {'password': {'write_only': True}}
