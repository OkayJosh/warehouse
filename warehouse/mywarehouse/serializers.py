from rest_framework import serializers

from .models import Inflow, Outflow

class InflowSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Inflow
        fields = ['name', 'quantity', 'comment']

class OutflowSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Outflow
        fields = ['name', 'quantity', 'comment']