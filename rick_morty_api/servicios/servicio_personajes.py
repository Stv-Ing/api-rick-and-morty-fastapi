import os
import requests

from dotenv import load_dotenv

load_dotenv()

URL_BASE = os.getenv("URL_BASE")


def obtener_datos_api(url):

    respuesta = requests.get(url)

    if respuesta.status_code != 200:
        return None

    return respuesta.json()