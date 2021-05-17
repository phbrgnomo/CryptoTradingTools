import pandas as pd
import btalib

asset = 'BTCUSDT'

# load DataFrame
asset_df = pd.read_csv(f'{asset}_bars3.csv', index_col=0)
# asset_df.set_index('date', inplace=True)
asset_df.index = pd.to_datetime(asset_df.index, unit='ms')

# calculate and print last RSI value
rsi = btalib.rsi(asset_df, period=14)
# print(rsi.df.rsi[-1])

#calculate and print macd
macd = btalib.macd(asset_df, pfast=20, pslow=50, psignal=13)
# print(macd.df)

# join the rsi and macd calculations as columns in original df
asset_df = asset_df.join([rsi.df, macd.df])
print(asset_df.tail())