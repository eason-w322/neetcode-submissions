class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        def solve(i):
            if i >= n:
                return 0
            
            if i in memo:
                return memo[i]
            
            result = cost[i] + min(solve(i+1), solve(i+2))
            memo[i] = result
            return result

        return min(solve(0), solve(1))