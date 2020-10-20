from rest_framework import serializers
from fishCultureApp.models import SWITCHES

class SWITCHESSerializer(serializers.ModelSerializer):
    class Meta:
        model = SWITCHES
        fields ='__all__'