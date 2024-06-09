from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'fullname', 'email', 'password', 'registration', 
                'role', 'region', 'created_at', 'is_active', 'is_staff', 'is_superuser',)
    
    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.fullname = validated_data['fullname']
        user.role = validated_data['role']
        user.registration = validated_data['registration']
        user.is_staff = False
        user.is_superuser = False
        if 'is_staff' in validated_data.keys():
            user.is_staff = validated_data['is_staff']
        if 'is_superuser' in validated_data.keys():
            user.is_superuser = validated_data['is_superuser']
        user.save()
        return user