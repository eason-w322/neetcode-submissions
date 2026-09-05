class Solution:
    def jump(self, nums: List[int]) -> int:
        furthest = 0
        jumps = 0
        right_end = 0
        if len(nums) == 1:
            return 0
        for i in range(len(nums)-1):
            furthest = max(furthest, i + nums[i])
            if i == right_end:
                jumps += 1
                right_end = furthest
        
        return jumps

            
        
        

        