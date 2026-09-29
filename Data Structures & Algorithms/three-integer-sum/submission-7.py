class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if target - nums[left] > nums[right]:
                    left += 1
                    continue
                if target - nums[left] < nums[right]:
                    right -= 1
                    continue
                if target - nums[left] == nums[right]:
                    results.append([-target, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return results
                    




        

                