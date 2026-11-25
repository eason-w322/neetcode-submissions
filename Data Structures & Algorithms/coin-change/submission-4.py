class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def solve(amount):
            if amount < 0:
                return float("inf")
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            
            best = float("inf")
            for c in coins:
                best = min(best, 1 + solve(amount - c))
            memo[amount] = best
            return best
        
        best = solve(amount)
        return best if best != float("inf") else -1
            

            

            
            
