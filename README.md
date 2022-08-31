# DJango B3 Asset Monitoring API

API de monitoramento de ativos da B3

Através dela é possível definir um plano de investimento. Isto é, definir um ponto de entrada e um ponto de saída para um determinado ativo. O monitoramente é feito de acordo com um intervalo determinado pelo usuário. Se a cotação atingir ou ultrapassar o valor de entrada, será enviado um e-mail recomendando a compra. Da mesma forma, se a cotação atingir o valor de saída, será enviado um e-mail recomendando a venda.

## Requisitos
- [VS code](https://code.visualstudio.com/download)
- [VS code remote containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)


## Ferramentas utilizadas
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Redis](https://redis.io/)
- [RQ:Workers](https://python-rq.org/docs/workers/)
- [Httpx](https://www.python-httpx.org/)
- [SQLite](https://www.sqlite.org/docs.html)
- [Pydantic](https://pydantic-docs.helpmanual.io/)

## Clone do projeto

```
  git clone git@github.com:MaiconRenildo/DJangoB3AssetMonitoringAPI.git
  cd DJangoB3AssetMonitoringAPI
```

  > <strong>Observações importantes</strong>: <ul><li>Antes de qualquer coisa é necessário preencher o arquivo <em>.env</em>  seguindo o padrão documentado no arquivo <em>.env.example</em>. Uma API key válida para a variável HG_API_KEY pode ser obtida no site da [HG brasil](https://hgbrasil.com/) </li><li>Para ter acesso ao ambiente de desenvolvimento configurado utilize o devcontainer por meio da [VS code remote containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)</li></ul>

## Configurações iniciais

Primeiramente é necessário criar as migrations. Para isso, abra o terminal do container de desenvolvimento e execute os comandos abaixo:

```
python manage.py makemigrations
python manage.py migrate
```
Para ter acesso ao ambiente administrativo, crie um super usuário através do comando:
```
python manage.py createsuperuser
```

## Execução

Para executar o projeto, acesse o terminal e execute os comandos abaixo em paralelo:
```
rq worker monitoring email --with-scheduler
python manage.py runserver --noreload
```
