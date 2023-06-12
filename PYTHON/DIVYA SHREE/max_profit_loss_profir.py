"""
    find the max profit that you can make by buying and selling in those days Example, 
    if the given array is [100, 180, 260, 310, 40, 535, 695], 
    the maximum profit can earned by buying on day 0, selling on day 3. 
    Again buy on day 4 and sell on day 6
    max_p = p buy = i sell = j
    """

prices = [100, 180, 260, 310, 40, 535, 695]

max_profit = 0
buy = 0
sell = 0

for i in range(len(prices)):
    for j in range(i+1, len(prices)):
        profit = prices[j] - prices[i]
        if profit > max_profit:
