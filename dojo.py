import os
import requests
import sys
import logging

logger = logging.getLogger()

path = 'http://localhost:8080'

logger.debug(f'O servidor esta em: {path}')

logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

data = {
    "username" : sys.argv[1],
    "password" : sys.argv[2]
}

logger.debug(f'Informacao sendo enviada {data}')

endpoint_get_token = os.path.join(path, 'auth/token/')

logger.debug(f'Requisitando token em: {endpoint_get_token}')
response = requests.post(
    endpoint_get_token,
    data=data
)

token = response.json()['token']

logger.info(f'Seu token e: f{token}')

cabecalho = {
    "Authorization" : "JWT %s" % token
}

logger.debug(f'Informacao no cabecalho JWT {cabecalho}')

endpoint_take_objetivo = os.path.join(path, 'take/take/objetivo')
response = requests.get(
    endpoint_take_objetivo,
    headers=cabecalho
)
logger.critical('DEU RUIM')
if response.status_code != 200:
    logger.critical('Requisicao nao foi feita com sucesso')
    raise Exception('Token nao foi coletado com sucesso')

logger.info(f'Informacao extraida da API: {response.json()}')
