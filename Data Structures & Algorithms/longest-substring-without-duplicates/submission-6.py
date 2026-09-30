class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        window = {}
        max_length = 0
        for right in range(len(s)):
            if s[right] not in window or window[s[right]] < left:
                window[s[right]] = right
                max_length = max(max_length, right - left + 1)
            else:
                left = window[s[right]] + 1
                window[s[right]] = right
        
        return max_length





            
            
            