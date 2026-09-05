class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        global_max = maximum
        for i in range(1, len(nums)):
            maximum = max(maximum + nums[i], nums[i])
            global_max = max(maximum, global_max)
        return global_max

            
            



            
        