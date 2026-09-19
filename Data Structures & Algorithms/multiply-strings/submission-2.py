class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m = len(num1)
        n = len(num2)

        results = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                p1 = i + j + 1
                p2 = i + j
                mul = int(num1[i]) * int(num2[j]) + results[p1]
                results[p1] = mul % 10
                results[p2] += mul // 10
        
        i = 0
        while i < len(results):
            if results[i] != 0:
                results = results[i:]
                break
            else:
                i += 1
        
        return "".join(str(i) for i in results)
        
        




        