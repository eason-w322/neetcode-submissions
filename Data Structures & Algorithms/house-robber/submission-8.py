class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        def solve(i):
            if i >= n:
                return 0
            if i == n - 1:
                return nums[i]
            if i in memo:
                return memo[i]
            result = max(solve(i+1), nums[i] + solve(i+2))
            memo[i] = result
            return result
        return solve(0)
            