from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password','is_verified']


class VerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Verify
        fields = ['email','otp']
