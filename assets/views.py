from rest_framework.response import Response
from rest_framework.views import APIView
from pydantic import BaseModel,Field
from rest_framework import request


class AssetMonitoringIn(BaseModel):
    asset_id:str = Field(...,example="f7d49390-cdb7-4a44-8fa4-235bfdddf113")
    upper_price_limit: float = Field(...,example= 50.0)
    lower_price_limit:float = Field(...,example=60.00) 
    id:str = Field(...,example="58d003ba-edb5-4ff6-a0e7-202a40aae494")
    interval:int = Field(...,example=3600)


class AssetMonitoring(APIView):

  def post(self,req:request):   
    """
      Rota responsável por habilitar o monitoramento de um ativo
    """
    from assets import config,utils
    
    monitoring_data = utils.get_monitoring_params(req)
      
    if monitoring_data == False: 
        return Response({"message":"Invalid params"},status=400)
  
    asset = utils.get_asset(monitoring_data.asset_id)

    config.enable_monitoring(asset_id=asset["id"])

    if asset == False:
      return Response({"message": "Asset Not found"  },status=404)

    if utils.register_monitoring(monitoring_data)  == False:
        return Response({"message": "asset already monitored"  },status=400)

    return Response({"message":"Monitoring enabled"})