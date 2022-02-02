from utils.keys import load_keys
import pandas as pd

# Load api keys from keys.yml
client = load_keys('binance')

asset = 'BTCUSDT'

# valid intervals - 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M
timeframe = '1d'

# get timestamp of earliest date data is available
timestamp = client._get_earliest_valid_timestamp(asset, timeframe)
print(f'Earliest timestamp for {asset} on the {timeframe} timeframe:', timestamp)

# request historical candle (or klines) data
bars = client.get_historical_klines(asset, timeframe, timestamp, limit=1000)

# keep 5 first fields (Date, open, high, low, close)
for line in bars:
    del line[5:]

# option 4 - create a Pandas DataFrame and export to CSV
asset_df = pd.DataFrame(bars, columns=['date', 'open', 'high', 'low', 'close'])
asset_df.set_index('date', inplace=True)
print(asset_df.head())

# export DataFrame to csv
asset_df.to_csv(f'{asset}_bars3.csv')

