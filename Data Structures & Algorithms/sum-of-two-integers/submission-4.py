class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 2**31 - 1

        while b:
            carry = (a & b) << 1 & MASK
            a = (a ^ b) & MASK
            b = carry
        
        return a if a <= INT_MAX else ~(a ^ MASK)
            