class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def solve(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if i in memo:
                return memo[i]
            result = solve(i+1) + solve(i+2)
            memo[i] = result
            return result
        
        return solve(0)