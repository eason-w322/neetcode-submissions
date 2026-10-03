class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        left = 0
        longest = 0

        for right in range(len(s)):
            if s[right] in window and window[s[right]] >= left:
                left = window[s[right]] + 1
                
            window[s[right]] = right
            longest = max(longest, right - left + 1)
        return longest




            
            
            