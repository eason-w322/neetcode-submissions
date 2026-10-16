class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        path = []
        seen = set()

        def backtrack():
            if len(path) == len(nums):
                results.append(path[:])
                return
            
            for i in range(0, len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                path.append(nums[i])
                backtrack()
                seen.remove(path.pop())
        
        backtrack()
        return results
        
