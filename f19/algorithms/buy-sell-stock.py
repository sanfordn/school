def maxProfit(prices):
    buyIndex = prices.index(min(prices))
    sellIndex = prices.index(max(prices[(buyIndex+1):]))
    if(prices[sellIndex] <= prices[buyIndex]):
        sellIndex = buyIndex
    
    print('buy: ' + str(buyIndex + 1) + ' sell: ' + str(sellIndex + 1) + ' ' + str(prices[sellIndex] - prices[buyIndex]))
    return prices[sellIndex] - prices[buyIndex]

maxProfit([7,1,5,3,6,4])
maxProfit([7,6,5,4,3,1])
