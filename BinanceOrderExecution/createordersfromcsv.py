from simplefunctions.load_keys import load_keys
import csv
from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceOrderException

### API
client = load_keys('binance')


# orders_file = input('What is the orders file name(.csv)?')
orders_file = 'orders.csv'

pair_index = 0
side_index = 1
type_index = 2
quantity_index = 3
order_price_index = 4


with open(orders_file) as file:
    csv_reader_object = csv.reader(file)
    if csv.Sniffer().has_header:
        next(csv_reader_object)
    for row in csv_reader_object:
        proposal_index = 0
        # print("CSV row: {0}".format(row))
        order_info = []
        pair = row[pair_index]
        side = row[side_index]
        type = row[type_index]
        quantity = float(row[quantity_index])
        order_price = float(row[order_price_index])
        # print(pair, side, type, quantity, order_price)
        try:
            buy_limit = client.create_order(
                symbol=pair,
                side=side,
                type=type,
                timeInForce='GTC',
                quantity=quantity,
                price=order_price)
            print(f'Order created! pair: {pair} side: {side} type: {type} amount: {quantity} price {order_price}')
        except BinanceAPIException as e:
            # error handling goes here
            print(e)
        except BinanceOrderException as e:
            # error handling goes here
            print(e)


'''
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
'''