class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def solve(i):
            if i >= n:
                return 0
            
            if i in memo:
                return memo[i]
            result = max(nums[i] + solve(i+2), solve(i+1))
            memo[i] = result
            return result
        return solve(0)
