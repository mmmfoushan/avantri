from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Job,WorkHistory

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

# Register Serializer
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

# Job Serializer
class JobSerializer(serializers.ModelSerializer):
	class Meta:
		model = Job
		fields ='__all__'

# WorkHistory Serializer
class WorkHistorySerializer(serializers.ModelSerializer):
	class Meta:
		model = WorkHistory
		fields ='__all__'