class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        right_end = 0
        furthest = 0
        n = len(nums)

        for i in range(n):
            furthest = max(furthest, nums[i] + i)
            if i == right_end and i < n-1:
                jumps += 1
                right_end = furthest
        
        return jumps
        
        

        