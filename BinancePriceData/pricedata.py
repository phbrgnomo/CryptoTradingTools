from simplefunctions.load_keys import load_keys

### API
client = load_keys('binance')
trading_pair = input('What trading pair your want to see the current price?')
# get latest price from Binance API
current_price = client.get_symbol_ticker(symbol=trading_pair)
# print full output (dictionary)
print(current_price)

# price lookup loop
value = True
while(value):
    current_price = client.get_symbol_ticker(symbol=trading_pair)
    # print full output (dictionary)
    print(current_price["price"])
