class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        window = {}
        max_frequency = 0
        longest_substring = 0
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            max_frequency = max(max_frequency, window[s[right]])
            if (right - left + 1) - max_frequency > k:
                window[s[left]] -= 1
                left += 1
            longest_substring = max(longest_substring, right - left + 1)
        return longest_substring
            
            