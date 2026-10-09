class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        left = 0
        length = len(nums3)
        right = length - 1
        mid = (left + right) // 2
        if right % 2 == 0:
            return nums3[mid]
        else:
            return (nums3[mid] + nums3[mid + 1])/2
        