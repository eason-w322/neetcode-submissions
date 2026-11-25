class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp1 = [0] * n
        dp2 = [0] * n

        dp1[0] = nums[0]
        dp2[0] = nums[0]

        for i in range(1,n):
            curr = nums[i]
            accumulate1 = dp1[i-1] * nums[i]
            accumulate2 = dp2[i-1] * nums[i]

            dp1[i] = max(curr, accumulate1, accumulate2)
            dp2[i] = min(curr, accumulate1, accumulate2)
        
        return max(dp1)