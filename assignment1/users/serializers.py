from rest_framework import serializers
from . models import *

class EmployeeReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeReferral
        fields=('__all__')