class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            last_digit = n % 2
            n = n//2
            if last_digit == 1:
                count += 1
        
        return count
