class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        if s[0] == "0":
            return 0
        if n == 1:
            return 1
        
        dp[0] = 1
        if int(s[0:2]) <= 26 and s[1] == "0":
            dp[1] = dp[0]
        elif int(s[0:2]) <= 26 and s[1] != "0":
            dp[1] = dp[0] + 1
        
        elif int(s[0:2]) > 26 and s[1] != "0":
            dp[1] = dp[0]

        elif int(s[0:2]) > 26 and s[1] == "0":
            dp[1] = 0

        for i in range(2, n):
            if s[i] != "0":
                dp[i] = dp[i-1]
            if s[i-1] != "0" and int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i-2]
        
        return dp[n-1]
            
