from hashlib import new
import utils.keys as keys
import ordermanagement.openorders as open_orders
import pprint
import pandas as pd

pp = pprint.PrettyPrinter(indent=4)

if __name__ == "__main__":
    
    # load api keys
    binance_api = keys.load_keys('binance')

    # set trading pairs
    pairs = ["NAVBTC", "FRONTBUSD", "PHBTUSD"]

    # store open orders from the pairs as a pandas dataframe
    open = open_orders.list_open_orders(binance_api, pairs)

    # calculate weighted average price
  
    open['value'] = open['size'].astype(float) * open['price'].astype(float)


    for p in pairs:
        sell_df = open.loc[(open['symbol'] == p) & (open['side'] == 'SELL')]
        buy_df = open.loc[(open['symbol'] == p) & (open['side'] == 'BUY')]
        sell_size = sell_df['size'].astype(float).sum()
        sell_price = sell_df['value'].sum() / sell_size
        buy_size = buy_df['size'].astype(float).sum()
        buy_price = buy_df['value'].sum() / buy_size
        print(f"{p} Sell Order - Size: {sell_size}, Price: {sell_price}")
        print(f"{p} Buy Order - Size: {buy_size}, Price: {buy_price}")
