class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left)//2
            candidate = nums[mid]
            if candidate == target:
                return mid

            elif candidate < target:
                left = mid + 1
            
            elif candidate > target:
                right = mid - 1
        
        return -1
