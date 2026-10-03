class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        window = {}
        max_freq = 0
        longest = 0

        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            max_freq = max(max_freq, window[s[right]])
            if (right - left + 1) - max_freq <= k:
                longest = max(longest, right - left + 1)
            else:
                window[s[left]] -= 1
                left += 1
        
        return longest



            
            