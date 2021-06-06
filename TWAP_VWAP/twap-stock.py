import yfinance as yf
import pandas as pd

# code source: https://blog.quantinsti.com/twap/

# import price data for Apple
data=yf.download('AAPL', start='2020-05-18', end='2020-06-18')
# print(data)

# calculate adjustment factor
adjustment_factor = data['Adj Close'] / data['Close']
# print(adjustment_factor)

# calculate adjusted open price
data['Adj Open'] = adjustment_factor * data['Open']
# print(data)

# calculate adjusted high price
data['Adj High'] = adjustment_factor * data['High']
# print(data)

# calculate adjusted low price
data['Adj Low'] = adjustment_factor * data['Low']
# print(data)

# Delete Volume column
del data['Close']
del data['Volume']
del data['Open']
del data['High']
del data['Low']
print(data)

# Fetch the averaged price of each trading day
# Use axis=1 for representing column
data['av_row'] = data.mean(axis=1)
print(data)

# Calculate twap
twap = data['av_row'].mean()
print('TWAP price on the last month:', twap)