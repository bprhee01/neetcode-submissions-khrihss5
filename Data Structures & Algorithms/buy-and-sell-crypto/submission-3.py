class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        currBuy = 0

        l = 0
        r = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
                continue
            diff = prices[r] - prices[l]
            maxP = max(maxP, diff)
            r += 1
        
        return maxP