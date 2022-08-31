from pydantic import BaseModel,Field
from urllib.request import Request

class AssetMonitoringIn(BaseModel):
    asset_id:str = Field(...,example="f7d49390-cdb7-4a44-8fa4-235bfdddf113")
    upper_price_limit: float = Field(...,example= 50.0)
    lower_price_limit:float = Field(...,example=60.00) 
    id:str = Field(...,example="58d003ba-edb5-4ff6-a0e7-202a40aae494")
    interval:int = Field(...,example=3600)


def register_monitoring(monitoring_data:AssetMonitoringIn):
    from assets.models import Monitoring,Asset
    try:
      Monitoring(
        asset_id =Asset(id=monitoring_data.asset_id),
        upper_price_limit=monitoring_data.upper_price_limit,
        lower_price_limit=monitoring_data.lower_price_limit,
        interval=monitoring_data.interval
      ).save()
      return True
    except:
      return False


def get_monitoring_params(req:Request):
    import ast
    try:
      body = dict(ast.literal_eval(req.body.decode("utf-8")))
      return AssetMonitoringIn(
        upper_price_limit=body['upper_price_limit'],
        lower_price_limit=body['lower_price_limit'],
        interval=body['interval'],
        asset_id=body['asset_id']
      )
    except:
      return False


def get_asset(asset_id):
    from assets.models import Asset
    try:
      return Asset.objects.filter(id=asset_id).values()[0]
    except:
      return False