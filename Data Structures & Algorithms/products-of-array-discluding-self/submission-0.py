class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = {}
        right = {}
        left[0] = nums[0]
        right[length - 1] = nums[-1]

        for i in range(1, length):
            left[i] = nums[i] * left[i-1]
        
        for j in range(length-2, -1, -1):
            right[j] = nums[j] * right[j+1]
        
        result = [0] * length
        for i in range(length):
            left_val = left[i-1] if i-1 in left else 1
            right_val = right[i + 1] if i+1 in right else 1
            result[i] = left_val * right_val
        
        return result
        
