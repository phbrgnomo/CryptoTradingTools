import yaml
from binance.client import Client
from pathlib import Path
from binance import ThreadedWebsocketManager

# Load API keys
def load_keys(exchange):
    if exchange == 'binance':
        key_pairs_file = Path('../keys.yml')
        with open(key_pairs_file, 'r') as keyfile:
            key_pair = yaml.safe_load(keyfile)
            client = Client(key_pair['binance']['binance_api_key'], key_pair['binance']['binance_api_secret'])
            return client

def load_websocket_keys(exchange):
    if exchange == 'binance':
        key_pairs_file = Path('../keys.yml')
        with open(key_pairs_file, 'r') as keyfile:
            key_pair = yaml.safe_load(keyfile)
            tws = ThreadedWebsocketManager(key_pair['binance']['binance_api_key'], key_pair['binance']['binance_api_secret'])
            return tws