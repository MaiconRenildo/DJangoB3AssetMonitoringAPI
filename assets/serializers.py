from rest_framework import serializers
from assets import models

class AssetSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Asset
    fields = ("code","company_name","CNPJ","id")

class MonitoringSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Monitoring
    fields = ("asset_id","upper_price_limit","lower_price_limit")