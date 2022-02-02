from utils.keys import load_keys, load_websocket_keys
from time import sleep
from binance.exceptions import BinanceAPIException, BinanceOrderException
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor

### API
client = load_websocket_keys('binance')

trading_pair = 'ETHUSDT'
price = {'BTCUSDT': None, 'error': False}

def btc_pairs_trade(msg):
    ''' define how to process incoming WebSocket messages '''
    if msg['e'] != 'error':
        price['BTCUSDT'] = float(msg['c'])
    else:
        price['error']:True

# starts websocket
bsm = BinanceSocketManager(client)
conn_key = bsm.start_symbol_ticker_socket('BTCUSDT', btc_pairs_trade)
bsm.start()

while not price['BTCUSDT']:
    # wait for WebSocket to start streaming data
    sleep(0.1)

# main trading logic
while True:
    # error check to make sure WebSocket is working
    if price['error']:
        # stop and restart socket
        bsm.stop_socket(conn_key)
        bsm.start()
        price['error'] = False

    else:
        if price['BTCUSDT'] > 10000:
            try:
                order = client.order_market_buy(symbol=trading_pair, quantity=100)
                break
            except BinanceAPIException as e:
                # error handling goes here
                print(e)
            except BinanceOrderException as e:
                # error handling goes here
                print(e)
    sleep(0.1)