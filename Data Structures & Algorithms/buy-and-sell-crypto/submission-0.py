class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        l = 0
        r = l + 1
        max_profit = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
                r += 1
        
        return max_profit