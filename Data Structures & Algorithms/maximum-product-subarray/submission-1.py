class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_dp = [0] * n
        min_dp = [0] * n
        min_dp[0] = max_dp[0] = nums[0]

        for i in range(1, n):
            c1, c2, c3 = nums[i], max_dp[i - 1] * nums[i], min_dp[i - 1] * nums[i]
            max_dp[i] = max(c1, c2, c3)
            min_dp[i] = min(c1, c2, c3)
        
        
        return max(max_dp)
        