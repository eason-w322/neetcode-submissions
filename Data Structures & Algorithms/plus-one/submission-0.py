class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        results = [1]
        i = len(digits) - 1
        while i >= 0 and digits[i] == 9:
            digits[i] = 0
            i -= 1
        
        if i == -1:
            digits.append(1)
            digits = digits[::-1]
        
        elif i == len(digits) - 1:
            digits[-1] += 1
        
        else:
            digits[i] += 1
        
        return digits
