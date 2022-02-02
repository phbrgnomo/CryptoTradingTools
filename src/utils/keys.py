import yaml
from binance.client import Client
from pathlib import Path
from binance import ThreadedWebsocketManager

key_pairs_file = Path('keys.yml')

# Check if keys are added to keys.yml
def check_keys(keypair, exchange):
    if keypair[f'{exchange}'][f'{exchange}_api_key'] == None:
        print(f"{exchange} api key not found! Check the keys.yml file")
        return False 
    if keypair[f'{exchange}'][f'{exchange}_api_secret'] == None:
        print(f"{exchange} api secret not found! Check the keys.yml file")
        return False
    return True

# Load API keys
def load_keys(exchange):
    with open(key_pairs_file, 'r') as keyfile:
        if exchange == 'binance':
            key_pair = yaml.safe_load(keyfile)
            if check_keys(key_pair, exchange) == False:
                return
            client = Client(key_pair['binance']['binance_api_key'], key_pair['binance']['binance_api_secret'])
            return client

def load_websocket_keys(exchange):
    if exchange == 'binance':
        with open(key_pairs_file, 'r') as keyfile:
            key_pair = yaml.safe_load(keyfile)
            if key_pair['binance']['binance_api_key'] or key_pair['binance']['binance_api_secret'] == None:
                return print(f"{exchange} keys not found!")   
            tws = ThreadedWebsocketManager(key_pair['binance']['binance_api_key'], key_pair['binance']['binance_api_secret'])
            return tws


