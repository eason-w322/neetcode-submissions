class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        index = n - 1
        while digits[index] == 9:
            digits[index] = 0
            index -= 1
            if index == -1:
                digits.append(1)
                digits = digits[::-1]
                return digits
        
        digits[index] += 1
        return digits
