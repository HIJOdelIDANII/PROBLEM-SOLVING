#i didn't use the sliding solutiuon for this one
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_price = 0
        max_difference = 0
        for i in range(len(prices)-1,-1,-1):
            if (max_price < prices[i]):
                max_price = prices[i]
            elif (max_price > prices[i]):
                max_difference = max(max_difference,max_price-prices[i])
        return max_difference
 
        