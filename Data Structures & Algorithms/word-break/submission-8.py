class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def solve(substring):
            if not substring:
                return True
            if substring in memo:
                return memo[substring]
            
            candidates = []
            for word in wordDict:
                length = len(word)
                if word == substring[0:length]:
                    candidates.append(length)
            
            if not candidates:
                return False
            
            result =  any(solve(substring[length:]) for length in candidates)
            memo[substring] = result
            return result
        
        
        return solve(s)
