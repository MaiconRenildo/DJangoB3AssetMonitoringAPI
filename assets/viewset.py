from rest_framework import viewsets,mixins
from assets import serializers,models


class AssetViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AssetSerializer
    queryset = models.Asset.objects.all()


class SimpleViewSet(
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
    ):
    pass


class MonitoringViewSet(SimpleViewSet):
    serializer_class = serializers.MonitoringSerializer
    queryset = models.Monitoring.objects.all()