import json
import os
import ssl
import requests
from urllib3.poolmanager import PoolManager
from requests.adapters import HTTPAdapter

class SSLAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = ssl.create_default_context()
        context.set_ciphers('TLSv1.2')
        kwargs['ssl_context'] = context
        return super().init_poolmanager(*args, **kwargs)

def create_ssl_session():
    session = requests.Session()
    session.mount('https://', SSLAdapter())
    return session

def update_json(filename, data):
     
    if os.path.exists(filename):
        with open(filename, "r") as f:
            current_data = json.load(f)
        current_data.update(data)
    else:
        save_json(filename, data)


def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_json(filename):
    with open(filename, "r") as f:
        return json.load(f)

