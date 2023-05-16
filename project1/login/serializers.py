from . models import *
from rest_framework import serializers




class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = ('__all__')

    