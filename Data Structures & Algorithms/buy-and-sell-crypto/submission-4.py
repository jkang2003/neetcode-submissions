class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        if len(prices) <= 1:
            return 0

        b = prices[0]
        for i in range(len(prices)):
            if(prices[i]<b):
                b = prices[i]
    
            if(prices[i] - b > 0):
                maxprofit = max(maxprofit, prices[i]-b)
        
        return maxprofit