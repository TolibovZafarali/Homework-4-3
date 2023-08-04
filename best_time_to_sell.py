class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        
        max_profit = 0
        min_price = prices[0]
        
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit


    
result = Solution()
print(result.maxProfit([7,1,5,3,6,4]))
print(result.maxProfit([7,6,4,3,1]))