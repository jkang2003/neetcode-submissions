class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        if len(prices) < 1:
            return maxprofit

        b = 0
        
        for s in range(len(prices)):
            if(prices[s] < prices[b]):
                b = s
            maxprofit = max(maxprofit, prices[s]-prices[b])

        return maxprofit