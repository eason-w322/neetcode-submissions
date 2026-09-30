class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = {}
        for c in s1:
            seen[c] = seen.get(c, 0) + 1
        length = len(s1)
        left = 0
        window = {}
        for right in range(len(s2)):
            window[s2[right]] = window.get(s2[right], 0) + 1
            if right >= length:
                window[s2[right - length]] -= 1
                if window[s2[right - length]] == 0:
                    del window[s2[right-length]]
            
            if window == seen:
                return True
        
        return False
            
            
