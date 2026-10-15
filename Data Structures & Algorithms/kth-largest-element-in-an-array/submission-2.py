class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return
        pivot = (0 + len(nums)) //2
        mid = nums[pivot]
        less = []
        equal = []
        larger = []
        for num in nums:
            if num < mid:
                less.append(num)
            elif num == mid:
                equal.append(num)
            else:
                larger.append(num)
        if len(larger) < k <= len(larger) + len(equal):
            return equal[0]
        elif len(larger) >= k:
            return self.findKthLargest(larger, k)
        else:
            return self.findKthLargest(less, k - len(larger) - len(equal))

