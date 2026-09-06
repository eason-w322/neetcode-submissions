class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        right_end = 0
        furthest = 0

        for i in range(len(nums)-1):
            furthest = max(furthest, nums[i] + i)
            if i == right_end:
                jumps += 1
                right_end = furthest
        
        return jumps
        
        

        