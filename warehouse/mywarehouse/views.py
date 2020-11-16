from rest_framework import viewsets

from .serializers import InflowSerializer, OutflowSerializer

from .models import Inflow, Outflow

class InflowViewSet(viewsets.ModelViewSet):
    serializer_class = InflowSerializer
    queryset = Inflow.objects.all()

class OutflowViewSet(viewsets.ModelViewSet):
    serializer_class = OutflowSerializer
    queryset = Outflow.objects.all()