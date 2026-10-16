class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        path = []
        def backtrack(index, path):
            results.append(path[:])

            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, path)
        return results
        


