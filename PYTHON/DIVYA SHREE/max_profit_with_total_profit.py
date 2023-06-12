share_price = [100, 180, 260, 310, 40, 535, 695]

total_profit = 0

# First transaction: buy on day 0, sell on day 3
buy_day_1 = 0
sell_day_1 = 3
profit_1 = share_price[sell_day_1] - share_price[buy_day_1]
total_profit += profit_1

# Second transaction: buy on day 4, sell on day 5
buy_day_2 = 4
sell_day_2 = 6
profit_2 = share_price[sell_day_2] - share_price[buy_day_2]
total_profit += profit_2

print("maximum profit is : ", max(profit_1, profit_2))
print("Total profit:", total_profit)
print("First transaction: Buy on day", buy_day_1, "and sell on day", sell_day_1)
print("Second transaction: Buy on day", buy_day_2, "and sell on day", sell_day_2)
