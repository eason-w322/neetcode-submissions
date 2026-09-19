class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        
        def helper(x, n):
            if n == 0:
                return 1.0
            product = helper(x, n//2)
            if n % 2 == 0:
                return product * product
            else:
                return product * product * x
        
        return helper(x, n)
