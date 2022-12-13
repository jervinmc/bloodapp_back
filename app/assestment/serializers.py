from rest_framework import serializers
from .models import Assestment

class AssestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Assestment
        fields="__all__"
