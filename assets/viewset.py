from assets import serializers,models
from rest_framework import viewsets


class AssetViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AssetSerializer
    queryset = models.Asset.objects.all()


class MonitoringViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MonitoringSerializer
    queryset = models.Monitoring.objects.all()