class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        offset = -1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid
        offset = left

        rotate_back = []
        for i in range(offset, len(nums) + offset):
            if i >= len(nums):
                i = i - len(nums)
            rotate_back.append(nums[i])
        
        left = 0
        right = len(rotate_back) - 1
        while left <= right:
            mid = (left + right) // 2
            if rotate_back[mid] == target:
                index = mid + offset
                if index >= len(nums):
                    index -= len(nums)
                return index
            
            elif rotate_back[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1









        