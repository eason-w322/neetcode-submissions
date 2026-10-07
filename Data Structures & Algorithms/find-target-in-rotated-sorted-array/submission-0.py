class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        offset = 0
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        offset = left
        result = []
        for i in range(offset, offset + len(nums)):
            if i >= len(nums):
                i = i - len(nums)
            result.append(nums[i])

        left = 0
        right = len(result) - 1
        while left <= right:
            mid = (left + right)//2
            if result[mid] == target:
                if mid + offset >= len(result):
                    return mid + offset - len(result)
                else:
                    return mid + offset
            elif result[mid] < target:
                left = mid + 1
            elif result[mid] > target:
                right = mid - 1
        return -1
            









        