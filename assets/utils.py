from assets import models

class AssetsRegister():

    def __init__(self):    
      self.not_exists = models.Asset.objects.exists() == False
    

    def get_assets(self):
      import httpx
      self.assets = httpx.get(
        url="https://api-cotacao-b3.labdo.it/api/empresa",
        timeout=60
      ).json()


    def insert(self):
      for asset in self.assets:

        codes = asset['cd_acao'].split(",")

        for code in codes:

          code = code.lstrip()
              
          if code != "":
            models.Asset.objects.get_or_create(
              code = code,
              company_name = asset['nm_empresa'],
              CNPJ = asset['vl_cnpj']
            )

      print("Dados dos ativos cadastrados com sucesso")