class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)] 

        best_start = 0
        best_length = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j+1-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if (j + 1 - i) > best_length:
                        best_length = j + 1 - i
                        best_start = i
        
        
        return s[best_start:best_start+best_length]
        
        