from simplefunctions.load_keys import load_keys


client = load_keys('binance')
print(client)
if client != '':
    print('keys found!')
