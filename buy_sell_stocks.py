prices =[7,1,5,3,6,4]
# min_price, profit = prices[0],0


# for p in prices:
#     if p <min_price:
#         min_price = p
#     elif p - min_price > profit:
#         profit = p - min_price

profit ,cur_profit = 0,0

cur_min_price = prices[0]

for p in prices:
    if p < cur_min_price:
        cur_min_price = p
    elif p - cur_min_price > cur_profit:
        cur_profit = p - cur_min_price
        profit += cur_profit
        cur_profit = 0
        cur_min_price = p

print(profit)