# Code Jam Challenge #1

## Objective:

Create a python script that executes the following tasks, with the following sequence:

1 - Pull the open orders on a specific trading pair on Binance

- The script must ask (input) what is the trading pair

2 - The following data of each open order must be stored to be used later on a calculation:

- `Order Size`
- `Order Price`
- `Order Quote Value` (Order size * Order Price)

3 - Cancel all open orders

4 - After all open orders are cancelled, do the following calculations

- `Order Size Sum`
- `Order Quote Value Sum`
- Calculate the `Merged Order Price` = `(Order Quote Value Sum) / (Order Size Sum)`

5 - Create a new Limit order on Binance where:

- `New Order Size` = `Order Size Sum`
- `New Order Price` = `Merged Order Price`
