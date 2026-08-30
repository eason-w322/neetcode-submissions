class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp_hold = [0] * n #hold at i
        dp_sold = [0] * n #sold the stock on day i
        dp_rest = [0] * n #not selling or buying

        dp_hold[0] = -prices[0]
        dp_sold[0] = 0
        dp_rest[0] = 0

        for i in range(1, n):
            dp_sold[i] = dp_hold[i-1] + prices[i]
            dp_hold[i] = max(dp_hold[i-1], dp_rest[i-1] - prices[i])
            dp_rest[i] = max(dp_rest[i-1], dp_sold[i-1])
        
        return max(dp_sold[n-1], dp_rest[n-1])


