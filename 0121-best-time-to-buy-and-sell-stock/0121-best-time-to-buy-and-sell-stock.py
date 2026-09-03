class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        max_profit = 0 
        minimum_prefix = prices[0]
        for i in range(1,len(prices)) : 
            profit = prices[i] - minimum_prefix 
            minimum_prefix = min(minimum_prefix , prices[i]) 
            max_profit = max(max_profit , profit) 
        return max_profit
           

        