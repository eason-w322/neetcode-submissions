class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def solve(i):
            if i in memo:
                return memo[i]
            
            if i == 2:
                return 2
            if i == 1:
                return 1
            
            result = solve(i - 1) + solve(i - 2)
            memo[i] = result
            return result
        return solve(n)

        
