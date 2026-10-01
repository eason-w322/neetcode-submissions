class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        output = []
        left = 0

        for right in range(len(nums)):
            while window and nums[window[-1]] < nums[right]:
                window.pop()

            window.append(right)
            if window[0] < left:
                window.popleft()

            if right - left + 1 == k:
                output.append(nums[window[0]])
                left += 1
        
        return output


        