import pandas as pd

def list_open_orders(exchange_api, pairs):
    
    df = pd.DataFrame({'symbol': [], 'side': [], 'size':[], 'price':[]})

    for p in pairs:
        
        orders = exchange_api.get_open_orders(symbol=p)
        for o in orders:
            df_orders = pd.DataFrame({'symbol': [o['symbol']], 'side': [o['side']], 'size': [o['origQty']], 'price': [o['price']]})
            df = pd.concat([df, df_orders])

        # df.to_csv('df.csv')
    return df
