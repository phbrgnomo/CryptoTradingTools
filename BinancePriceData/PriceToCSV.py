from simplefunctions.load_keys import load_keys
import csv
from datetime import datetime


client = load_keys('binance')

asset = 'ETHUSDT'

# valid intervals - 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M
timeframe = '1d'

# get timestamp of earliest date data is available
timestamp = client._get_earliest_valid_timestamp(asset, timeframe)
print(f'Earliest timestamp for {asset} on the {timeframe} timeframe:', timestamp)

# request historical candle (or klines) data
bars = client.get_historical_klines(asset, timeframe, timestamp, limit=1000)

# option 2 - save as CSV file using the csv writer library
with open(f'{asset}_bars.csv', 'w', newline='') as f:
    wr = csv.writer(f)
    for line in bars:
        wr.writerow(line)

# option 3 - save as CSV file without using a library.
with open(f'{asset}_bars2.csv', 'w') as d:
    for line in bars:
        d.write(f'{line[0]}, {line[1]}, {line[2]}, {line[3]}, {line[4]}\n') # This only saves the first 4 values: date, open, high, low, close