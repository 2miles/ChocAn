from typing import Optional
import json
import os

class ProviderService:
    def __init__(self, data : dict):
        self.code = data['code']
        self.fee  = data['fee']
        self.name = data['name']

def _get_provider_directory() -> list[dict]:
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, './prov_dir.json')
    return json.load(open(filename, 'r'))

# TODO
def generate_provider_directory() -> None:
    pass

def get_provider_service(code : int) -> Optional['ProviderService']:
    provider_services = _get_provider_directory()
    provider_service = next((ProviderService(p) for p in provider_services if p['code'] == code), None)
    return provider_service