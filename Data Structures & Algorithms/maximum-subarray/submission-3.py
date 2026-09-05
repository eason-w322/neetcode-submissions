class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        def solve(i):
            if i == 0:
                return nums[0]
            if i in memo:
                return memo[i]
            
            result = max(solve(i-1)+nums[i], nums[i])
            memo[i] = result
            return result
        
        return max([solve(i) for i in range(0, n)])
            



            
        