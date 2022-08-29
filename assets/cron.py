def is_market_closed():
    from datetime import datetime
    import pytz
    hour = datetime.now(tz=pytz.timezone("Brazil/East")).hour
    week_day = datetime.now(tz=pytz.timezone("Brazil/East")).weekday()

    if week_day == 5 or week_day == 6:
        return True

    return True if hour < 10 or hour>17 else False


def user_email():
    import os,dotenv
    dotenv.load_dotenv(dotenv.find_dotenv())
    return os.getenv('USER_EMAIL')


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
        return False


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


def exec_monitoring(asset_id:str):
    import os,django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'b3assetmonitoring.settings')
    django.setup()

    from assets.queue import monitoring_queue,email_queue
    from assets.models import Asset,Monitoring
    from datetime import timedelta

    monitoring = Monitoring.objects.get(asset_id=asset_id)    
    asset = Asset.objects.get(id=asset_id)

    monitoring_queue().enqueue_in(timedelta(minutes=monitoring.interval),exec_monitoring,asset_id=asset_id)

    if is_market_closed(): return False

    cotation = get_asset_cotation(asset.code)

    if cotation == False: return False
    
    if monitoring.lower_price_limit <= cotation and monitoring.upper_price_limit > cotation:
      if monitoring.buy_order == None:
        email_queue().enqueue(
          send_purchase_recommendation_email,
          email=user_email(),
          asset_code=asset.code,
          price=cotation
        )

        monitoring.buy_order = True
        monitoring.save()

    if monitoring.upper_price_limit <= cotation:
      if monitoring.sell_order == None:
        email_queue().enqueue(
          send_sale_recommendation_email,
          email=user_email(),
          asset_code=asset.code,
          price=cotation
        )

        monitoring.sell_order = True
        monitoring.save()