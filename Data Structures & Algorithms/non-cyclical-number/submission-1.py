class Solution:
    def isHappy(self, n: int) -> bool:
        def square_digit_sum(n):
            total = 0
            while n > 0:
                last_digit = n % 10
                total += last_digit * last_digit
                n = n // 10
            return total
        
        seen = set()
        while n > 0:
            output = square_digit_sum(n)
            if output == 1:
                return True
            if output in seen:
                return False
            seen.add(output)
            n = output
