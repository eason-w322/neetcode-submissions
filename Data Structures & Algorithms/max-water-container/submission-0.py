class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        max_area = 0
        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            max_area = max(area, max_area)
            l_bound = heights[left]
            r_bound = heights[right]

            if l_bound > r_bound:
                right -= 1
            
            else:
                left += 1


        return max_area



