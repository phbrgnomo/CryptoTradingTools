from simplefunctions.load_keys import load_keys
from simplefunctions.questions import yn

### API
client = load_keys('binance')

show_balance = yn('Show full account balance?')

# Show total account balance, ignoring savings tokens
if show_balance == True:
    # get balances for all assets & some account information
    full_info = client.get_account()
    balances = full_info['balances']
    for i in range(len(balances)):
        asset_info = dict(balances[i])
        asset = asset_info['asset']
        free_amount = float(asset_info['free'])
        locked_amount = float(asset_info['locked'])
        total_amount = free_amount + locked_amount
        if total_amount == 0:
            continue
        if (asset[0] + asset[1]) == 'LD':
            continue
        print('Asset:', asset, '\tTotal Balance:', total_amount, '\tAmount locked in orders:', locked_amount)

if show_balance == False:
    try:
        token = input('What token you want the information? ')
        # get balance for a specific asset only (BTC)
        asset_balance = client.get_asset_balance(asset=token)
        asset = asset_balance['asset']
        free_amount = float(asset_balance['free'])
        locked_amount = float(asset_balance['locked'])
        total_amount = free_amount + locked_amount
        print('Asset:', asset, '\tTotal Balance:', total_amount, '\tAmount locked in orders:', locked_amount)
    except:
        print("Invalid Token.")

# get balances for futures account
# print(client.futures_account_balance())

# get balances for margin account
# print(client.get_margin_account())

# avgprice = client.get_avg_price(symbol="BTCUSDT")
# print(avgprice)
