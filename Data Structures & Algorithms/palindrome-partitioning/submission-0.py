class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []
        path = []

        def backtrack(index):
            if index == len(s):
                results.append(path[:])
                return 

            for i in range(index + 1, len(s) + 1):
                substring = s[index:i]
                if substring == substring[::-1]:
                    path.append(substring)
                    backtrack(i)
                    path.pop()
        
        backtrack(0)
        return results
            

