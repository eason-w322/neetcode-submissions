class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def solve(remaining):
            if remaining == "":
                return True
            if remaining in memo:
                return memo[remaining]
            
            candidates = []
            for word in wordDict:
                length = len(word)
                if remaining[0:length] == word:
                    candidates.append(length)
            
            result = any(solve(remaining[i:]) for i in candidates)
            memo[remaining] = result
            return result
        
        return solve(s)


