class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        results = []
        elements = deque()
        for right in range(len(nums)):
            if elements and elements[0] < left:
                elements.popleft()
            
            
            while elements and nums[elements[-1]] < nums[right]:
                elements.pop()
            elements.append(right)


            if right - left + 1 == k:
                results.append(nums[elements[0]])
                left += 1
            
        return results
            


        