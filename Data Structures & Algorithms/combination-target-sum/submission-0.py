class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        path = []

        def backtrack(index, target):
            if target == 0:
                results.append(path[:])
                return
            elif target < 0:
                return
            
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i, target - nums[i])
                path.pop()
        
        backtrack(0, target)
        return results