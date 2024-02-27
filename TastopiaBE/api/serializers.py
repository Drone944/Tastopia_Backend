from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        password = serializers.CharField(write_only=True)
        model = User
        fields = ['id', 'username', 'password', 'email']