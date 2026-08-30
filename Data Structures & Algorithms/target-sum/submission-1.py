class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def backtrack(i, total):
            if i == n:
                if total == target:
                    return 1
                return 0
            
            if (i, total) in memo:
                return memo[(i, total)]
            
            add = backtrack(i+1, total + nums[i])
            sub = backtrack(i+1, total - nums[i])
            result = add + sub
            memo[(i, total)] = result
            return result
        
        return backtrack(0, 0)
        