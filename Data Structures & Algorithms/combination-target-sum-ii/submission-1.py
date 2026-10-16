class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        path = []
        candidates.sort()
        def backtrack(index, target):
            if target == 0:
                results.append(path[:])
                return
            elif target < 0:
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i])
                path.pop()

        backtrack(0, target)
        return results