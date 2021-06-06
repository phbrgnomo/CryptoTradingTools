from simplefunctions.load_keys import load_keys
from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceOrderException

### API
client = load_keys('binance')

trading_pair = 'BTCUSDT'

# Create limit order
# for test pourposes, change client.create_order to client.create_test_order
# create a real order if the test orders did not raise an exception

try:
    buy_limit = client.create_order(
        symbol=trading_pair,
        side='BUY',
        type='LIMIT',
        timeInForce='GTC',
        quantity=0.001,
        price=32000)

except BinanceAPIException as e:
    # error handling goes here
    print(e)
except BinanceOrderException as e:
    # error handling goes here
    print(e)

# same order but with helper function
# buy_limit = client.order_limit_buy(symbol='ETHUSDT', quantity=100, price=200)

# market order using a helper function
# market_order = client.order_market_sell(symbol='ETHUSDT', quantity=100)