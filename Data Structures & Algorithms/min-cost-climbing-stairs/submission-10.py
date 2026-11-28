class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        def solve(i):
            if i >= n:
                return 0
            if i == n - 1:
                return cost[n-1]
            
            if i in memo:
                return memo[i]
            
            result = min(solve(i+1) + cost[i], solve(i+2) + cost[i])
            memo[i] = result
            return result
        
        return min(solve(0), solve(1))
            

