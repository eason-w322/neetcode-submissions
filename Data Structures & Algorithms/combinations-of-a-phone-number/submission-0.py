class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        numbers = {}
        numbers["2"] = "abc"
        numbers["3"] = "def"
        numbers["4"] = "ghi"
        numbers["5"] = "jkl"
        numbers["6"] = "mno"
        numbers["7"] = "pqrs"
        numbers["8"] = "tuv"
        numbers["9"] = "wxyz"

        results = []
        path = []

        def backtrack(index):
            if index == len(digits):
                results.append("".join(path[:]))
                return
            
            for i in range(0, len(numbers[digits[index]])):
                path.append(numbers[digits[index]][i])
                backtrack(index + 1)
                path.pop()
        backtrack(0)
        return results

