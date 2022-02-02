from utils.keys import load_keys
import json
from datetime import datetime


client = load_keys('binance')

asset = 'BTCUSDT'

# valid intervals - 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M
timeframe = '1d'

# get timestamp of earliest date data is available
timestamp = client._get_earliest_valid_timestamp(asset, timeframe)
print(f'Earliest timestamp for {asset} on the {timeframe} timeframe:', timestamp)

# request historical candle (or klines) data
bars = client.get_historical_klines(asset, timeframe, timestamp, limit=1000)

# option 1 - save to file using json method
with open(f'{asset}_bars.json', 'w') as e:
    json.dump(bars, e)

# option 5 - save to file using json method keeping 5 first fields (Date, open, high, low, close)
with open(f'{asset}_bars2.json', 'w') as e:
    for line in bars:
        del line[5:]
    json.dump(bars, e)