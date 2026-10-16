class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        path = []

        total = n * 2
        def backtrack(left, right):
            if len(path) == total:
                results.append("".join(path[:]))
                return
            
            if left < n:
                path.append("(")
                backtrack(left + 1, right)
                path.pop()
            
            if right < left:
                path.append(")")
                backtrack(left, right + 1)
                path.pop()
        
        backtrack(0, 0)
        return results