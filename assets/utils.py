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


def get_asset_cotation(code:str):
    import httpx,os,dotenv
    dotenv.load_dotenv(dotenv.find_dotenv())
    response = httpx.get(
        url="https://api.hgbrasil.com/finance/stock_price?key=" + os.getenv("HG_API_KEY") + "&symbol=" + code,
        timeout=60
    ).json()['results']

    try:
        return response[code.upper()]['price']
    except:
        raise Exception("Code note found")


def send_purchase_recommendation_email(asset_code:str,price:float,email:str):
    from assets.email import send

    return send(
        to=email,
        subject="Recomendação de compra - " + asset_code,
        msg="A cotação atual do ativo é de R$ " + str(price) + " . Conforme os parâmetros de monitoramento, sugerimos a compra." 
    )


def send_sale_recommendation_email(asset_code:str,price:float,email:str):
    from assets.email import send
    return send(
        to=email,
        subject="Recomendação de venda - " + asset_code,
        msg="A cotação atual do ativo é de R$ " + str(price) + " . Conforme os parâmetros de monitoramento, sugerimos a venda." 
    )