class Solution:
    def minWindow(self, s: str, t: str) -> str:
        seen = {}
        for c in t:
            seen[c] = seen.get(c, 0) + 1
        
        match = len(seen)
        formed = 0
        left = 0
        window = {}
        shortest = ""
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            if s[right] in seen and window[s[right]] == seen[s[right]]:
                formed += 1
            while formed == match:
                if len(shortest) > len(s[left:right+1]) or shortest == "":
                    shortest = s[left:right+1]

                window[s[left]] -= 1
                if s[left] in seen and window[s[left]] < seen[s[left]]:
                    formed -= 1
                left += 1
                
            
        
        return shortest
            


            










            
        

