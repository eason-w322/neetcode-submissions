class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = {}
        for c in s1:
            seen[c] = seen.get(c, 0) + 1
        
        window = {}
        left = 0
        length = len(s1)
        for right in range(len(s2)):
            if s2[right] not in seen:
                window = {}
                left = right + 1
                continue
            
            window[s2[right]] = window.get(s2[right], 0) + 1
            if window == seen:
                return True
    
            if window[s2[right]] > seen[s2[right]]:
                window[s2[left]] -= 1
                left += 1
        return False
            

            
