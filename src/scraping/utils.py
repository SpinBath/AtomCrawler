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

        with open(filename, "r", encoding="utf-8") as f:
            current_data = json.load(f)

        if isinstance(current_data, list):
            if isinstance(data, list):
                current_data.extend(data)

        elif isinstance(current_data, dict):
            if isinstance(data, dict):
                current_data.update(data)
        
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(current_data, f, ensure_ascii=False, indent=4)
    else:
        save_json(filename, data)

def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_json(filename):
    with open(filename, "r") as f:
        return json.load(f)

