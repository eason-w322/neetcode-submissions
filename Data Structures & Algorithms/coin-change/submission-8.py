class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount
        dp = [float("inf")] * (n + 1)

        dp[0] = 0
        for i in range(1, n+1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], dp[i-c] + 1)
        
        return dp[n] if dp[n] != float("inf") else -1

            

            
            
