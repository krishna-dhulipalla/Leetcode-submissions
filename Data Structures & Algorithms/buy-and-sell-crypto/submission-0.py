class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minvalue = prices[0]
        maxprofit = 0

        for i in prices[1:]:
            maxprofit = max(maxprofit, i - minvalue)
            minvalue = min(minvalue, i)
            
        return maxprofit