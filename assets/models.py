from django.db import models
from uuid import uuid4

class Asset(models.Model):
    id =  models.UUIDField(primary_key=True,default=uuid4,editable=False)
    code = models.CharField(null=False,unique=True,max_length=10)
    company_name = models.CharField(null=False,unique=False,max_length=10)
    CNPJ = models.CharField(null=False,unique=False,max_length=15)


class Monitoring(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4,editable=False,unique=True)
    asset_id = models.ForeignKey(to=Asset,on_delete=models.CASCADE)
    upper_price_limit = models.FloatField(verbose_name="upper_price_limit")
    lower_price_limit = models.FloatField(verbose_name="lower_price_limit")
    created_at = models.DateField(auto_now_add=True)
    buy_order = models.BooleanField(null=True)
    sell_order = models.BooleanField(null=True)