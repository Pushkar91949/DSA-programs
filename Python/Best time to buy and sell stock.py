# 1 <= prices.length <= 105
# 0 <= prices[i] <= 10**4

# TIME COMPLEXITY = O(n)

def maxProfit(prices):

    min_price = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]

        if prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
