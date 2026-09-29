class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        left = 0
        for i in range(len(height)):
            left = max(height[i], left)
            left_max[i] = left

        right_max = [0] * n
        right = 0
        for i in range(len(height)-1, -1, -1):
            right = max(height[i], right)
            right_max[i] = right
        
        total = 0
        for i in range(len(height)):
            total += min(right_max[i], left_max[i]) - height[i]
        
        return total