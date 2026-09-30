class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        window = {}
        longest_length = 0
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            if sum(window.values()) - max(window.values()) > k:
                window[s[left]] -= 1
                left += 1
            longest_length = max(longest_length, sum(window.values()))
        return longest_length
            
            
            