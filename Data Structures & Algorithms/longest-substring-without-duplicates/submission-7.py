class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        window = {}
        longest_length = 0
        for right in range(len(s)):
            if s[right] in window and window[s[right]] >= left:
                left = window[s[right]] + 1
            window[s[right]] = right
            longest_length = max(longest_length, right - left + 1)
        
        return longest_length





            
            
            