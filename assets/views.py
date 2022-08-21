from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import request

class AllAssets(APIView):

  def post(self,req:request):
    """
      Rota responsável por automatizar a inserção de todos os ativos
    """
    from assets.utils import AssetsRegister
    
    assets_data = AssetsRegister()

    if assets_data.not_exists:
      assets_data.get_assets()
      assets_data.insert()
      return Response({
        "message":"Assets registered successfully"
      })
    else:
      return Response({
        "message":"Assets already registered"
      })