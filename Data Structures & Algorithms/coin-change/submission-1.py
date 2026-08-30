class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float("inf")] * (amount + 1) for _ in range(n + 1)]
        for i in range(n+1):
            dp[i][0] = 0

        for i in range(n+1):
            for j in range(amount+1):
                dp[i][j] = dp[i-1][j]
                if coins[i-1] <= j:
                    dp[i][j] = min(dp[i][j], dp[i][j - coins[i-1]] + 1)
        
        return dp[n][amount] if dp[n][amount] != float("inf") else -1