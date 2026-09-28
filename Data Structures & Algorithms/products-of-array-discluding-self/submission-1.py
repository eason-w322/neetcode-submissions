class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = [0] * len(nums)
        l_mul = 1
        for i in range(len(nums)):
            results[i] = l_mul
            l_mul = l_mul * nums[i]
        
        r_mul = 1
        for i in range(len(nums)-1, -1, -1):
            results[i] = results[i] * r_mul
            r_mul = r_mul * nums[i]
        
        return results

