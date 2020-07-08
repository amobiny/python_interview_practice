

def get_max_profit(stock_prices):
    max_profit = stock_prices[1] - stock_prices[0]
    min_price = stock_prices[0]
    for i in range(2, len(stock_prices)):
        current = stock_prices[i]
        max_profit = max(max_profit, current-min_price)
        min_price = min(min_price, current)

    return max_profit


stock_prices = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices)
# Returns 6 (buying for $5 and selling for $11)
