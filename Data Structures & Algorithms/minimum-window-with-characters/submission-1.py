class Solution:
    def minWindow(self, s: str, t: str) -> str:
        seen = {}
        for c in t:
            seen[c] = seen.get(c, 0) + 1
        minimum_sub = ""
        left = 0
        needed = len(seen)
        window = {}
        formed = 0

        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            if s[right] in seen and window[s[right]] == seen[s[right]]:
                formed += 1
            
            while formed == needed:
                if minimum_sub == "" or len(minimum_sub) > right - left + 1:
                    minimum_sub = s[left:right+1]
                window[s[left]] -= 1
                if s[left] in seen and window[s[left]] < seen[s[left]]:
                    formed -= 1
                left += 1
            
        return minimum_sub
                
                









            
        

