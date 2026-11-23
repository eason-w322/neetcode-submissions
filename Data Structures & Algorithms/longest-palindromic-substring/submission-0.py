class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        
        best = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                if substring == substring[::-1]:
                    if len(substring) > len(best):
                        best = substring
        
        return best