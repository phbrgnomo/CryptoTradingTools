import pandas as pd
import btalib

asset = 'BTCUSDT'

# load DataFrame
asset_df = pd.read_csv(f'{asset}_bars3.csv', index_col=0)
# asset_df.set_index('date', inplace=True)
asset_df.index = pd.to_datetime(asset_df.index, unit='ms')

sma = btalib.sma(asset_df.close)
print(sma.df)

# create sma and attach as column to original df
asset_df['sma'] = btalib.sma(asset_df.close, period=20).df
print(asset_df.tail())