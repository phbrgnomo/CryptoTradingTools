import pandas as pd

asset = 'BTCUSDT'

# load DataFrame
asset_df = pd.read_csv(f'{asset}_bars3.csv', index_col=0)
# asset_df.set_index('date', inplace=True)
asset_df.index = pd.to_datetime(asset_df.index, unit='ms')

# calculate 20 SMA using Pandas
asset_df['20sma'] = asset_df.close.rolling(20).mean()
print(asset_df.tail(10))

# calculate just the last value for the 20 moving average
mean = asset_df.close.tail(20).mean()
print(f'current 20 SMA: {mean}')

# get the highest closing price in 2020
year = '2021'
max_val = asset_df.close[year].max()
print(f'Max price of the year {year}: {max_val}')
