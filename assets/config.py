class AssetsRegister():
    
    def __init__(self): 
      from assets import models   
      self.not_exists = models.Asset.objects.exists() == False
    

    def get_assets(self):
      import httpx
      self.assets = httpx.get(
        url="https://api-cotacao-b3.labdo.it/api/empresa",
        timeout=60
      ).json()


    def insert(self):
      from assets import models
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


def enable_monitoring(asset_id:str):
    import os
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'b3assetmonitoring.settings')
    from assets.queue import monitoring_queue
    from assets.cron import exec_monitoring
    monitoring_queue().enqueue(exec_monitoring,asset_id=asset_id)


def start_crons():
    from assets.models import Monitoring
    
    assets_monitoring = Monitoring.objects.all().values()

    for asset in assets_monitoring:
        enable_monitoring(asset['asset_id_id'])


def insert_assets():   
    assets_data = AssetsRegister()

    if assets_data.not_exists:
      assets_data.get_assets()
      assets_data.insert()
      print("\nAssets registered successfully\n")
    else:
      print("\nAssets already registered\n")