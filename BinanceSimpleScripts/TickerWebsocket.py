from simplefunctions.load_keys import load_websocket_keys

# set variables
asset='ETHUSDT'
asset_price = {'error':False}


def pair_trade_history(msg):
    # define how to proccess incoming WebSocket messages
    if msg['e'] != 'error':
        print(f'{asset} timestamp:', msg['E'], '\n'
              f'{asset} last price:', msg['c'],'\n'
              f'{asset} best bid:', msg['b'],'\n'
              f'{asset} best ask:', msg['a'],'\n')
        asset_price['last'] = msg['c']
        asset_price['bid'] = msg['b']
        asset_price['ask'] = msg['a']
    else:
        asset_price['error'] = True

# init and start the WebSocket
bsm = load_websocket_keys('binance')
bsm.start()
bsm.start_symbol_ticker_socket(callback=pair_trade_history, symbol=asset)

