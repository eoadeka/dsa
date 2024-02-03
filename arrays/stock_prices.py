
stock_prices = [ 298, 305, 320, 301, 292 ]

for i in range(len(stock_prices)):
    if stock_prices[i] == 301:
        print(i) 

print(stock_prices[2])

stock_prices.insert(1, 285)
print(stock_prices)