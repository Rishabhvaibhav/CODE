"""
    find the max profit that you can make by buying and selling in those days Example, 
    if the given array is [100, 180, 260, 310, 40, 535, 695], 
    the maximum profit can earned by buying on day 0, selling on day 3. 
    Again buy on day 4 and sell on day 6
     
"""

share_price = [100, 180, 260, 310, 40, 535, 695]


max_profit = 0
day_when_buy = 0
day_when_sell = 0
for i in range(len(share_price)):
    if share_price[i] < share_price[day_when_buy]:   
        day_when_buy = i
    else:    
        day_when_sell = i
max_profit = share_price[day_when_sell] - share_price[day_when_buy]

print("Maximum profit is :", max_profit)
print("The day when buy share", day_when_buy, "and That day when Sell that share ", day_when_sell)