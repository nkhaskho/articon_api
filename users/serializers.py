from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'fullname', 'email', 'password', 'registration', 
                'role', 'region', 'created_at', 'is_active', 'is_staff',)
    
    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.fullname = validated_data['fullname']
        user.registration = validated_data['registration']
        user.save()
        return user