import logging
import requests
import sys
import os

from pathlib import Path

class Logger:

    def __init__(self, level):

        formatter = logging.Formatter(
            '[%(asctime)-15s][%(levelname)s] - %(message)s'
        )

        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)

        self._logger = logging.getLogger('mylogger')
        self._logger.setLevel(level)
        self._logger.addHandler(handler)

    def get_logger(self):
        return self._logger

logger = Logger(logging.INFO).get_logger()

def verify_status_code(response, code = 200):

    if response.status_code != code:
        logger.critical('Erro ao acessar o servidor')
        raise Exception(
            f'Receive status code {response.status_code} not {code}\n{response.json()}'
        )

API_PATH = 'http://localhost:8080'

if __name__ == '__main__':
    
    logger.info("Iniciando requisição do token")
    logger.debug("Carregando credenciais")

    auth_data = {
        "username": sys.argv[1],
        "password": sys.argv[2]
    }
    
    logger.debug("Authentication header: {auth_header}")

    auth_endpoint = os.path.join(API_PATH, 'auth/token/') 
    logger.debug(f'API path resolved {auth_endpoint}')
    response = requests.post(
        auth_endpoint,
        data=auth_data
    )

    verify_status_code(response)

    token = response.json()['token']

    logger.info(f'Token requisitado com sucesso')
    logger.info('Iniciando requisicao para extrair informação')


    objetivo_endpoint = os.path.join(API_PATH, 'take/take/objetivo/')

    logger.debug(f'Endpoint para objetivo: {objetivo_endpoint}')
    headers = {
        'Authorization' : f"JWT {token}"
    }

    logger.debug(f'Header de authenticacao {headers}')

    response = requests.get(
        objetivo_endpoint,
        headers=headers
    )

    verify_status_code(response)

    logger.info(response.json())
